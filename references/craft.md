# CV craft cheat-sheet

The reusable best bits pulled from the strongest resume tools and skills surveyed (dabydat resume-builder, the resume-tailoring skills, the software-engineer reviewer, Jobscan/ATS-refinement, ats-screener, Resume-Matcher). Use these when scoring category 3 (impact) and category 6 (fit), and when suggesting fixes.

## Bullet formulas (score adherence, don't force a template)
- **XYZ (Google):** "Accomplished [X] as measured by [Y], by doing [Z]." Every bullet should have an X and ideally a Y.
- **Verb + Action + Result:** open on a strong past-tense verb, state the action, end on the measurable result.
- **STAR** for the two or three flagship bullets: Situation, Task, Action, Result — but compressed, results-forward.
- Lead with the outcome when it's strong ("Cut cycle time 90%…"), the method second.
- One idea per bullet. No bullet without a noun the reader can picture.

## What real ATS parsers do (from ats-screener's platform simulation)
- Parse by **section header** then by **date-anchored role blocks**. Non-standard headers ("What I've done") can misparse — keep at least one conventional header per section.
- **Tables, columns, text boxes, headers/footers** are where parsing breaks. Single flowing column is safest.
- Keyword matching is **literal and often stemmed**, not semantic: if the JD says "Kubernetes" and the CV says "k8s" only, some parsers miss it. Include the spelled-out term at least once.
- Dates need a machine-readable **month/year range** per role.
- Skills are matched both in a Skills section and inline in experience — having a keyword in both helps.

## Tailoring vs spray (from the tailoring skills + commercial-tool caveats)
- **Spray (job boards, no JD):** optimise for a strong generic CV with broad, truthful keyword coverage of the target domain. Don't over-tune to one ATS config. A mid-range match on many roles beats a perfect match on one.
- **Targeted (specific JD):** mirror the JD's own nouns where truthful, close the top missing keywords, and reorder bullets so the most JD-relevant sit first. Never invent to close a gap — surface the gap to the candidate instead.

## Engineering-manager signals recruiters look for
- Team **size and trajectory** ("6 engineers, 12 at peak across two teams").
- **People outcomes**: promotions, mentoring, retention, hiring bar.
- **Delivery** in numbers: velocity, reliability, incident command, OKR hit-rate.
- **Scope**: budget, headcount, product/discipline ownership, stakeholder altitude (Product, Exec).
- **Business impact** in £/revenue/cost, not just engineering internals.
- Enough hands-on signal to be credible without reading as an IC who happens to manage.

## Red flags that cost points
- Vague duties instead of achievements; "responsible for…" with no result.
- Buzzwords with no evidence (see slop list in cv_signals.py).
- AI-generated tone: em-dash clusters, rule-of-three everywhere, tidy-list-with-payoff cadence. Run the natural-writing linter.
- Inconsistent tense/formatting; missing or fuzzy dates; unexplained gaps.
- Over-claiming — the fastest way to lose a recruiter's trust, and a hard rule never to coach the candidate toward.
