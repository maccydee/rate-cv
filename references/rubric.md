# The CV scoring rubric (100 points)

Weighted for **engineering-leadership** CVs, UK market. Built from recruiter scorecards, ATS-vendor guidance, and EM-resume best practice. The mechanical categories are fed by `cv_signals.py`; the judgement categories you score yourself from the extracted text.

Score each category, sum, subtract deductions, clamp to 0–100. Always return a per-category breakdown so the number is auditable — a bare score is useless.

## Categories

### 1. ATS parse-ability — 15 pts (mechanical, from signals)
- File format text-based (.docx / text PDF), single-flow, **no tables/columns** — 4
- Standard section headers present (Experience, Education, Skills, Summary) — 4
- Every role has a clear month/year **date range**, no unexplained gaps — 4
- Complete contact block (email, phone, LinkedIn) — 3

### 2. Structure & clarity — 12 pts
- Length fits seniority (EM: 2 pages ideal, 3 max) — 3
- Clean hierarchy, scannable, consistent formatting — 3
- Chronological clarity, most recent first — 3
- No grammar/spelling errors — 3

### 3. Quantified impact — 20 pts (partly mechanical)
- **≥60% of achievement bullets carry a metric** (%, £, time, count) — 7 (signal: `quantification_pct`)
- Claims are specific and verifiable, not vague ("improved efficiency") — 6
- Bullets follow **Action → Scope → Outcome** (XYZ / "did X, measured by Y, via Z") — 4 (signal: `action_verb_pct` is a proxy)
- Metrics are credible and traceable, not inflated — 3

### 4. Engineering-leadership signals — 28 pts (the decisive block)
People & talent (10): team size + growth stated; promotions/mentoring/retention; hiring/interview ownership.
Delivery & execution (9): velocity/quality/reliability metrics; roadmap & OKR delivery; incident ownership.
Strategic & org impact (9): tech-debt/architecture calls; process & culture (OKRs, on-call, standards, DX); **business impact linked to £/revenue/cost**.

### 5. Seniority & scope — 15 pts
- Clear IC→EM→(senior) progression — 4
- Explicit scope ownership (headcount, budget, product area, discipline) — 4
- Domain depth shown concretely ("platform serving N req/day") — 4
- Relevant education/certs (or strong experience substitute) — 3

### 6. Role fit & communication — 10 pts
- People/process/strategy bias (not all-IC-code) for an EM role — 4
- Cross-functional collaboration (Product, Exec, other functions) — 3
- Clear, jargon-controlled writing — 3

## Deductions (cap −15)
- AI-slop present: em-dash clusters, slop terms, or natural-writing FAIL — up to −5 (signals: `em_dash_count`, `slop_terms_found`, linter)
- Unexplained employment gap >6 months — −3
- Missing dates on any role — −2
- Unverifiable / inflated claims (any) — −5  *(hard line: never coach the candidate toward fabrication)*
- No quantification anywhere — −3
- Job-hopping unexplained (3+ moves in 2 yrs) — −3

## Bands
- 90–100 shortlist-strong · 75–89 qualified · 60–74 borderline, needs work · 45–59 below bar · <45 rework

## Dual score (only when a JD is supplied)
Report the rubric score **and**, separately, a JD-match read from `jd_match`:
- **ATS keyword match %** (`match_pct`) and the **missing keywords** worth adding *if truthful*.
- **Qualification fit**: your judgement of whether the CV evidences the JD's core must-haves — call each met / partial / gap.
Keep the two apart: a CV can be well-written (high rubric) yet a poor JD match (low fit), and vice-versa.
