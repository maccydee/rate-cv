# rate-cv

[![Claude skill](https://img.shields.io/badge/Claude-skill-8A2BE2.svg)](https://docs.claude.com/en/docs/claude-code/skills)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Claude Code [skill](https://docs.claude.com/en/docs/claude-code/skills) that rates and critiques a CV/resume: it scores the document out of 100 against a weighted engineering-leadership rubric, checks ATS parse-ability, quantified impact, and AI-slop, and can match the CV to a specific job description with a keyword gap list.

The score is a sanity check, not truth. Real ATS platforms don't emit a score a recruiter sees, and commercial checkers disagree by ~20 points on the same file. So the skill leads with an auditable per-category breakdown and specific, coaching-framed fixes, not just a number.

## What it does

- **Standalone quality** (no job description): how strong the CV is for engineering-leadership roles, and what would raise it.
- **Targeted match** (job description supplied): the above, plus a separate ATS keyword match and qualification-fit read against that role.
- **Mechanical signals** from `scripts/cv_signals.py`: ATS parse-ability (format, single-flow vs tables/columns, section headers, dated roles, contact block), quantification density, action-verb usage, em-dash count, AI-slop terms, and JD keyword overlap.
- **Writing quality** via an optional natural-writing linter pass, if present at `~/.claude/skills/natural-writing`.
- **Judgement categories** (leadership signals, impact specificity, seniority, fit) scored against `references/rubric.md`, using the bullet formulas and ATS rules in `references/craft.md`.

It never coaches toward fabrication: if a job wants a keyword the candidate can't truthfully claim, it reports a gap rather than suggesting you invent it.

## Install

```bash
git clone https://github.com/maccydee/rate-cv.git ~/.claude/skills/rate-cv
```

Then in Claude Code, run `/rate-cv` (or just ask it to "rate my CV"). Works on `.docx` and `.txt`; for PDFs, extract the text first.

## Layout

```
rate-cv/
  SKILL.md              orchestration + workflow
  scripts/cv_signals.py mechanical signal engine (.docx/.txt, optional --jd)
  references/rubric.md   the weighted 100-point scoring rubric
  references/craft.md    bullet formulas + real-ATS parse rules + red flags
```

## The rubric (100 points)

ATS parse-ability 15 · structure & clarity 12 · quantified impact 20 · **engineering-leadership signals 28** · seniority & scope 15 · role fit & communication 10, with deductions (cap −15) for AI-slop, unexplained gaps, missing dates, and unverifiable claims. Bands: 90+ shortlist-strong, 75–89 qualified, 60–74 borderline.

## Usage from the command line

The signal engine runs standalone too:

```bash
python3 scripts/cv_signals.py path/to/CV.docx
python3 scripts/cv_signals.py path/to/CV.docx --jd job-description.txt
python3 scripts/cv_signals.py path/to/CV.docx --json
```

## Licence

MIT.
