---
name: rate-cv
description: Rate and critique a CV/resume. Scores it out of 100 against a weighted engineering-leadership rubric, checks ATS parse-ability, quantified impact, and AI-slop, and can match it to a specific job description with a keyword gap list. Use this whenever the user wants a CV or resume rated, scored, graded, reviewed, critiqued, checked against ATS, or matched to a job posting, and also when they ask to improve, tighten, or sanity-check a CV even if they don't literally say "rate". Works on .docx and .txt; pass a job description too for a targeted match.
---

# rate-cv

Score a CV honestly and specifically, then hand back a number that's auditable and fixes that are actionable. Two modes:

- **Standalone quality** (no JD): how strong is this CV for engineering-leadership roles, and what would raise it.
- **Targeted match** (JD supplied): the above **plus** a separate ATS keyword match and qualification-fit read against that job.

The number is a sanity check, not truth — real ATS platforms don't emit a score a recruiter sees, and web tools disagree by ~20 points on the same file. So always lead with the breakdown and the fixes, and say what the score does and doesn't mean.

## Hard rules
- **Never coach toward fabrication.** If a job description wants a keyword the candidate can't truthfully claim, report it as a gap; do not suggest inventing experience, titles, or scope. This is the line that separates honest CV help from the tools that quietly tell people to lie.
- **Watch for AI-slop** in anything you rewrite: clustered em-dashes, rule-of-three everywhere, tidy-list-with-payoff cadence. If a `natural-writing` skill is installed, route rewritten prose through it; otherwise apply the same judgement yourself.
- Score from evidence in the file, not assumptions. If the file won't parse, say so rather than guessing.

## Workflow

1. **Locate the CV.** Get the file path from the user or from the conversation (if they attached or just generated one, use that). If they only say "my CV" and there's no obvious file, ask for the path rather than guessing. If it's a PDF, extract text first (e.g. with the `pdf` skill), then point this skill at the `.txt`.

2. **Run the signal engine.**
   ```bash
   python3 ~/.claude/skills/rate-cv/scripts/cv_signals.py <cv-file> [--jd <jd.txt>]
   ```
   It prints ATS parse-ability, quantification %, action-verb %, em-dash count, slop terms, contact/dates/sections, and (with `--jd`) keyword match % + missing keywords. It also writes `<cv>.extracted.txt`.
   To feed a JD, save the pasted job description to a temp `.txt` first, then pass `--jd`.

3. **Run the writing linter** on the extracted prose:
   ```bash
   python3 ~/.claude/skills/natural-writing/scripts/detect.py <cv-file>.extracted.txt
   ```
   Its slop score and any FAILs feed the deductions in the rubric.

4. **Read the extracted text yourself** and score the judgement categories in `references/rubric.md` (leadership signals, impact specificity, seniority, fit) that no script can measure. Use `references/craft.md` for what earns vs loses points and for the bullet formulas (XYZ / Verb-Action-Result). The mechanical categories come straight from the signals.

5. **Compute the score.** Sum the six categories, apply deductions (cap −15), clamp 0–100. Map to a band.

6. **Report** in this order:
   - **Score /100 and band**, with a one-line "what this means / doesn't mean".
   - **Category breakdown** table (points earned / max, one phrase each).
   - **Top 3 strengths** — concrete, quoting the CV.
   - **Top 3–5 fixes** — specific and coaching-framed ("add team size to the Deloitte role", not "improve leadership signals"), each with the points it would recover. If you propose a reworded bullet, make it truthful and em-dash-free.
   - **If JD supplied:** a separate **JD match** block — keyword match %, the missing keywords worth adding *if truthful*, and a met/partial/gap read on the JD's core must-haves. Keep it apart from the rubric score.
   - **External cross-check** (optional, one line): suggest a free second opinion (Resume Worded for writing, sunnypatell/ats-screener for real-ATS parse) and remind that tool scores are noisy.

## Notes
- `cv_signals.py` counts explicit achievement bullets; also read the experience prose for metrics the bullet counter won't catch, and factor that into category 3.
- Keep the whole thing under a screen where possible — a tight, ranked answer beats an exhaustive audit.
- This skill rates and advises; it does not silently rewrite the CV. Offer to apply fixes as a follow-up.
