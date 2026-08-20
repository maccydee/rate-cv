# The CV scoring rubric (100 points)

Weighted for **leadership CVs in any field**, UK market. Categories 1-3 (47
points) are domain-neutral. Categories 4-6 (53 points) are about leading
people and owning scope, which every profession has, but the *evidence* differs
by field: a nurse educator's equivalent of "incident ownership" is a serious
incident review, and their equivalent of "platform serving N req/day" is a
caseload or a cohort size.

**Read the domain off the CV before you score, name it in the output, and use
the mapping table under category 4.** Do not silently re-invent the rubric for
each CV: an unstated adaptation produces a number that looks comparable and
is not. Built from recruiter scorecards, ATS-vendor guidance, and EM-resume best practice. The mechanical categories are fed by `cv_signals.py`; the judgement categories you score yourself from the extracted text.

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

### 4. Leadership signals — 28 pts (the decisive block)

**People & talent (10):** for an individual contributor, read this as
influence rather than headcount: who they trained, whose work they reviewed,
what they set the standard for. A senior IC with no reports can score here;
scoring them zero because the rubric expects a team is how a good analyst
looks like a weak leader.

Team or cohort size stated with growth; developing
others, with evidence (promotions, progression, retention, qualification
pass rates); ownership of recruitment or selection.

**Delivery & execution (9):** measured outcomes in the field's own units;
delivery against a plan or cycle; ownership when things go wrong.

**Strategic & org impact (9):** decisions that changed how the organisation
works, not just what it produced; standards, process or policy they set;
**impact tied to money, risk, or a regulated outcome**.

What counts as evidence, by field:

| | Delivery measured as | Ownership when it goes wrong | Strategic impact |
|---|---|---|---|
| Engineering | velocity, quality, reliability | incident command, on-call | architecture and tech-debt calls, DX |
| Clinical / nursing | caseload, cohort size, audit results, competency sign-offs | serious incident review, safeguarding escalation | policy or guideline authorship, CQC or accreditation outcomes |
| Teaching | cohort outcomes, progress measures, intervention results | safeguarding, behaviour escalation | curriculum design, whole-school policy |
| Finance / accounting | close cycle time, variance, audit findings | control failures, remediation | policy, controls framework, systems change |
| Operations | throughput, cost per unit, SLA | escalation ownership, root cause | process redesign, supplier or contract strategy |
| Data / analytics | model or report adoption, data quality measures, decision impact | pipeline failures, incorrect numbers shipped | data model or warehouse design, governance and definitions |
| Fundraising / charity | funds raised, retention, conversion, grant sizes | funder relationships at risk, compliance | case for support, portfolio or channel strategy |

If a field is not listed, name the equivalents explicitly in your output before
scoring, so the reader can see what you counted.

### 5. Seniority & scope — 15 pts
- Clear progression into and through leadership (practitioner → lead → senior),
  whatever the field's ladder is called — 4
- Explicit scope ownership: headcount, budget, caseload, department, site,
  discipline — 4
- Domain depth shown concretely, in the field's own units ("platform serving
  N req/day", "18-bed paediatric HDU", "£40m portfolio", "cohort of 240") — 4
- Relevant qualifications, registration or certification where the field
  requires it (NMC PIN, QTS, ACA/CIMA, chartership), or a strong experience
  substitute where it does not — 3

### 6. Role fit & communication — 10 pts
- Bias matches the role applied for: a leadership CV that reads as pure
  hands-on practice is a mismatch, and so is a practitioner CV that has lost
  all clinical or technical credibility — 4
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
