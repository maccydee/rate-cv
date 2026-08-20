# The CV scoring rubric (100 points)

Weighted for **leadership CVs in any field**, UK market. Categories 1-3 and 7 (51
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

### 2. Structure & clarity — 8 pts
- Length fits seniority (EM: 2 pages ideal, 3 max) — 2
- Clean hierarchy, scannable, consistent formatting — 2
- Chronological clarity, most recent first — 2
- No grammar/spelling errors — 2

### 3. Quantified impact — 20 pts (partly mechanical)
- **≥60% of achievement bullets carry a metric** (%, £, time, count) — 7 (signal: `quantification_pct`)
- Claims are specific and verifiable, not vague ("improved efficiency") — 6
- Bullets follow **Action → Scope → Outcome** (XYZ / "did X, measured by Y, via Z") — 4 (signal: `action_verb_pct` is a proxy)
- Metrics are credible and traceable, not inflated — 3

### 4. Leadership signals — 24 pts (the decisive block)

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
| Marketing / comms | pipeline, MQL to SQL conversion, CAC, campaign revenue, share of voice | a campaign that missed, budget overspend, a public misstep | positioning, channel mix, brand or category strategy |
| Legal / in-house counsel | matters closed, contract cycle time, risk exposure reduced | disputes, regulatory findings, escalation to the board | policy and playbook authorship, contracting framework |
| Policy / public sector | submissions cleared, consultations run, legislation or guidance landed | ministerial risk, delivery failure, public scrutiny | policy design, cross-department negotiation |
| Hospitality / retail ops | covers, net sales, GP%, labour%, NPS, site count | a site underperforming, a food-safety or licensing issue | format, supply or estate strategy |
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

### 7. Currency — 8 pts

How recent the evidence is, which nothing else in this rubric measures. A CV
can be immaculately structured, fully quantified and entirely about work that
stopped three years ago, and every other category will score it well. The gap
itself is not the problem: a career break is a fact, and this rubric refuses to
penalise honesty about one. What decides the shortlist is whether the tools,
regulations and practices on the page are still the ones in use.

- **Tools, systems and practices evidenced in the last 24 months** — 4. Score
  what the CV actually shows in date, not what the person could probably still
  do. Name the ones that have lapsed.
- **Retired, renamed or superseded items presented as current** — 2. Check
  them: Universal Analytics stopped processing in July 2023, Google Optimize
  closed in September 2023, Data Studio is Looker Studio, Twitter Ads is X Ads.
  In regulated fields the equivalents are registrations, mandatory training and
  framework versions. Award the points when nothing on the CV is stale; deduct
  proportionally when things are, and **say which**.
- **Recent evidence exists at all** — 2. Voluntary, freelance, contract,
  trustee, study, open-source. A current self-run programme with a number
  attached is the strongest available answer to a break, and it is worth asking
  for one before concluding it does not exist.

Report this element separately in the headline, not folded into the total:
`72/100 · currency 3/8`. A single number let a CV with a three-and-a-half year
break and three dead platforms on it come back 94/100, band "shortlist-strong",
while the same document's own notes said the fit was much weaker. The number
people read has to carry the thing that will decide the outcome.

An honest gap costs nothing here. Stale evidence costs points, and the person
can act on that: refresh a tool, take a course, put a current number on
voluntary work. Being scored down for a break they cannot undo teaches them
nothing.

## Deductions (cap −15)
- AI-slop present: em-dash clusters, slop terms, or natural-writing FAIL — up to −5 (signals: `em_dash_count`, `slop_terms_found`, linter)
- Unexplained employment gap >6 months — −3  *(explained is not penalised: see category 7, which scores currency instead)*
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
