#!/usr/bin/env python3
"""
cv_signals.py — mechanical signal extraction for the rate-cv skill.

Extracts plain text from a CV (.docx / .txt / .md) and computes the objective,
countable signals a human shouldn't eyeball: ATS parse-ability, quantification
density, bullet-formula adherence, AI-slop terms, length, contact block, and
(optionally) keyword match against a pasted job description.

The LLM does the *judgement* categories (leadership signals, impact specificity)
using references/rubric.md. This script only supplies the facts.

Usage:
  python3 cv_signals.py <cv-file> [--jd <jd-file>] [--json]
Writes <cv>.extracted.txt (plain prose) for the natural-writing linter.
Prints a human-readable signal report, or strict JSON with --json.
"""
import sys, os, re, json, zipfile, html

STOP = set("a an the and or but if then else for to of in on at by with from as is are was were be been being this that these those it its it's you your we our i my he she they them his her their at into over under out up down not no yes do does did will would can could should may might must have has had a about above after again against all am any because before below between both during each few more most other some such only own same so than too very s t can".split())

SLOP = ["leverage","leveraged","leveraging","synergy","synergies","spearhead","spearheaded",
        "pivotal","intricate","seamless","seamlessly","robust","utilize","utilized","utilise",
        "delve","underscore","showcase","foster","garner","myriad","plethora","tapestry",
        "cutting-edge","best-in-class","results-driven","detail-oriented","team player",
        "go-getter","thought leader","synergize","holistic","paradigm","bleeding-edge",
        "dynamic professional","proven track record","hit the ground running"]

STRONG_VERBS = set("""led built shipped drove cut reduced grew scaled owned launched delivered
designed created removed automated migrated hired coached mentored ran managed increased
decreased improved saved raised took chaired authored governed codified established
implemented rearchitected refactored consolidated negotiated recovered resolved streamlined
partnered forecast forecasted planned prioritised prioritized rolled deployed integrated""".split())

SECTION_ALIASES = {
 "summary":   ["profile","summary","about","personal statement","professional summary"],
 "experience":["experience","employment","work history","career history","professional experience"],
 "education": ["education","qualifications","academic","certifications","training"],
 "skills":    ["skills","technical skills","core skills","competencies","expertise","technologies"],
}

# ---------- extraction ----------
def docx_text(path):
    z = zipfile.ZipFile(path)
    xml = z.read("word/document.xml").decode("utf-8", "ignore")
    has_tables = "<w:tbl" in xml
    # paragraph = <w:p ...> ... </w:p>; text = the <w:t> runs inside
    paras = []
    for pm in re.findall(r"<w:p[ >].*?</w:p>", xml, re.S):
        runs = re.findall(r"<w:t[^>]*>(.*?)</w:t>", pm, re.S)
        txt = html.unescape("".join(runs)).strip()
        paras.append(txt)
    return paras, has_tables

def plain_paras(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".docx":
        return docx_text(path)
    if ext in (".txt", ".md"):
        raw = open(path, encoding="utf-8", errors="ignore").read()
        return [l.strip() for l in raw.splitlines()], False
    raise SystemExit(f"Unsupported file type {ext}. Convert to .docx or .txt first (PDFs: use the pdf skill to extract text).")

# ---------- signals ----------
BULLET_GLYPHS = "•·▪‣◦-–*"
def is_bullet(p):
    return len(p) > 1 and p[0] in BULLET_GLYPHS

# generic CV/JD filler that isn't a real skill keyword — filtered so "missing keywords" stays sharp
JD_FILLER = set("""team teams role roles work working experience experienced year years ability able
strong good great excellent including include includes required requirement requirements responsible
responsibilities skills skill knowledge understanding etc looking join company companies business
candidate candidates ideal preferred plus nice must proven track record ownership owner build building
help helping ensure across within using use used within world class high level within growth impact
opportunity opportunities environment fast paced culture people person new well like want need across""".split())

def keywords(text, top=40):
    toks = re.findall(r"[a-zA-Z][a-zA-Z+.#-]{1,}", text.lower())
    freq = {}
    for t in toks:
        t = t.strip(".-")
        if len(t) < 3 or t in STOP or t in JD_FILLER: continue
        freq[t] = freq.get(t, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda x: -x[1])[:top]]

def analyse(path, jd_path=None):
    paras, has_tables = plain_paras(path)
    nonempty = [p for p in paras if p]
    full = "\n".join(nonempty)
    low = full.lower()
    words = re.findall(r"\S+", full)
    wc = len(words)

    # content/achievement lines: explicit bullets, else medium-length non-heading lines
    bullets = [p.lstrip(BULLET_GLYPHS).strip() for p in nonempty if is_bullet(p)]
    if not bullets:
        bullets = [p for p in nonempty if 40 <= len(p) <= 400 and not p.isupper()]

    def has_number(s):
        return bool(re.search(r"\d|£|\$|%|\bpercent\b|\bx\b|times", s.lower()))
    quant = sum(1 for b in bullets if has_number(b))
    verb_start = sum(1 for b in bullets if b.split() and re.sub(r"[^a-z]","",b.split()[0].lower()) in STRONG_VERBS)

    sections = {}
    for key, aliases in SECTION_ALIASES.items():
        sections[key] = any(re.search(r"(?im)^\W{0,3}(%s)\b" % "|".join(aliases), full) or a in low for a in aliases)

    contact = {
        "email": bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", full)),
        "phone": bool(re.search(r"(\+?\d[\d ()-]{7,}\d)", full)),
        "linkedin": "linkedin.com" in low,
    }
    dates = re.findall(r"\b(19|20)\d{2}\b", full)
    # linear-safe: anchor on the start year; optional single month token before the end year (no ReDoS)
    date_ranges = len(re.findall(r"(?:19|20)\d{2}\s*[-–—]\s*(?:[a-z]{3,9}\s)?(?:present|current|now|(?:19|20)\d{2})", low))
    em_dashes = full.count("—")
    slop_hits = sorted({w for w in SLOP if re.search(r"\b"+re.escape(w)+r"\b", low)})

    sig = {
        "file": os.path.basename(path),
        "format": os.path.splitext(path)[1].lower().lstrip("."),
        "word_count": wc,
        "est_pages": round(wc / 500, 1),
        "has_tables_or_columns": has_tables,
        "sections_found": {k: v for k, v in sections.items()},
        "missing_sections": [k for k, v in sections.items() if not v],
        "contact_block": contact,
        "year_tokens": len(dates),
        "explicit_date_ranges": date_ranges,
        "bullets_detected": len(bullets),
        "bullets_with_metric": quant,
        "quantification_pct": round(100 * quant / len(bullets)) if bullets else 0,
        "bullets_action_verb_lead": verb_start,
        "action_verb_pct": round(100 * verb_start / len(bullets)) if bullets else 0,
        "em_dash_count": em_dashes,
        "slop_terms_found": slop_hits,
    }

    if jd_path:
        jd = open(jd_path, encoding="utf-8", errors="ignore").read()
        jd_kw = keywords(jd, top=40)
        matched = [k for k in jd_kw if re.search(r"\b"+re.escape(k)+r"\b", low)]
        missing = [k for k in jd_kw if k not in matched]
        sig["jd_match"] = {
            "jd_keywords_considered": len(jd_kw),
            "matched": matched,
            "missing": missing,
            "match_pct": round(100 * len(matched) / len(jd_kw)) if jd_kw else 0,
        }

    # write extracted prose for the natural-writing linter
    out_txt = path + ".extracted.txt"
    open(out_txt, "w", encoding="utf-8").write(full)
    sig["_extracted_text_path"] = out_txt
    sig["_full_text"] = full
    return sig

def report(sig):
    L = []
    L.append(f"CV SIGNALS · {sig['file']}  ({sig['format']}, ~{sig['est_pages']} page(s), {sig['word_count']} words)")
    L.append("")
    L.append("ATS parse-ability")
    L.append(f"  format: {sig['format']}  " + ("[!] tables/columns present — can break parsers" if sig['has_tables_or_columns'] else "single-flow (good)"))
    L.append(f"  sections: found {[k for k,v in sig['sections_found'].items() if v]}" + (f"  MISSING {sig['missing_sections']}" if sig['missing_sections'] else ""))
    c = sig['contact_block']; L.append(f"  contact: email={c['email']} phone={c['phone']} linkedin={c['linkedin']}")
    L.append(f"  dates: {sig['year_tokens']} year tokens, {sig['explicit_date_ranges']} explicit role date-ranges")
    L.append("")
    L.append("Impact & writing")
    L.append(f"  bullets detected: {sig['bullets_detected']}")
    L.append(f"  quantified: {sig['bullets_with_metric']}/{sig['bullets_detected']} = {sig['quantification_pct']}%  (target >=60%)")
    L.append(f"  action-verb lead: {sig['action_verb_pct']}%")
    L.append(f"  em-dashes: {sig['em_dash_count']}  (clustered em-dashes are a common AI tell)")
    L.append(f"  slop terms: {sig['slop_terms_found'] or 'none'}")
    if "jd_match" in sig:
        j = sig["jd_match"]
        L.append("")
        L.append(f"JD keyword match: {j['match_pct']}%  ({len(j['matched'])}/{j['jd_keywords_considered']})")
        L.append(f"  MISSING (add if truthful): {', '.join(j['missing'][:20])}")
    L.append("")
    L.append(f"[extracted prose written to {sig['_extracted_text_path']} — run natural-writing detect.py on it]")
    return "\n".join(L)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        raise SystemExit("usage: cv_signals.py <cv-file> [--jd <jd-file>] [--json]")
    cv = args[0]; jd = None; as_json = "--json" in args
    if "--jd" in args:
        jd = args[args.index("--jd") + 1]
    sig = analyse(cv, jd)
    if as_json:
        print(json.dumps({k: v for k, v in sig.items() if k != "_full_text"}, indent=2))
    else:
        print(report(sig))
