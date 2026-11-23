# Week 1 plan: November 23–29, 2026

## Week objective

Finish and validate one complete decision-support flow that the whole team can run locally:

```text
Synthetic room data → validation → budget filter → TOPSIS ranking → top-three explanation → tests
```

This is a working baseline, not the final application. The team should avoid login, maps, scraping, payment, machine learning, and other optional features during this week.

## Decisions to confirm at the first meeting

The proposed answers are already reflected in the starter repository. The team should either confirm them or record a replacement by November 23.

| Question | Proposed answer | Reason |
| --- | --- | --- |
| What problem are we solving? | Student housing selection near a defined campus/area | Clear user, alternatives, and measurable criteria |
| Which technique will we use? | TOPSIS | Ranks alternatives using user-defined priorities; no ML training required |
| Which course concept does it support? | Model-driven DSS | The course introduces DSS categories; TOPSIS is an additional method researched by the team |
| Web or desktop? | Local web app | Easier to share, demo, revise, and run on a second computer |
| Language and framework? | Python + Streamlit | One language for the interface, validation, and ranking algorithm |
| What data will we use first? | Clearly labelled synthetic data | Fast to validate; no scraping, consent, or source-quality uncertainty |
| Project language? | English | Interface, documentation, report, slides, comments, and demo script |
| Which criteria? | Monthly cost, distance, area, security, amenities | Two cost criteria and three benefit criteria |

If the team does not agree with any proposed answer, write the replacement in the issue or meeting note before changing code.

## Individual work plans

Each task has one owner. If a task needs information or a code change from someone else, the owner contacts that person directly; this plan does not assign assistants or reviewers.

### Hồ Ngọc An — requirements and data

| Date | Task | Deliverable |
| --- | --- | --- |
| Mon, Nov 23 | Confirm the decision problem, target users, five criteria, units, and cost/benefit directions | A one-page requirement note and a finalized data dictionary in `data/README.md` |
| Tue, Nov 24 | Expand the sample CSV from 8 to at least 30 synthetic room records | A UTF-8 CSV with unique IDs, English names, and `synthetic` in every source field |
| Wed, Nov 25 | Audit the expanded dataset against the schema | A short validation checklist: no missing fields, duplicate IDs, invalid scores, negative values, or zero cost/area |
| Thu, Nov 26 | Document the scoring rules for security and amenities | Explicit 1–5 scoring rules in the data dictionary |
| Fri, Nov 27 | Prepare the report input: problem statement, user needs, dataset description, and assumptions | A draft in `docs/` ready to reuse in the final report |
| Sat, Nov 28 | Run a final data validation after any schema changes | Dataset passes the application validator |
| Sun, Nov 29 | Publish the data work in a pull request | One PR containing only data and data-documentation changes |

### Châu Thành Phát — TOPSIS method

| Date | Task | Deliverable |
| --- | --- | --- |
| Mon, Nov 23 | Create a manually calculated example using three rooms and the five agreed criteria | A table showing the decision matrix, weights, normalized values, ideal solutions, D+, D-, C, and final ranking |
| Tue, Nov 24 | Compare the manual example against `rank_rooms` | The same ranking and scores within the documented rounding rule |
| Wed, Nov 25 | Document the TOPSIS procedure and the treatment of cost and benefit criteria | A concise methodology note in `docs/` for the report and slides |
| Thu, Nov 26 | Define three weight profiles: budget-focused, campus-focused, and space/amenities-focused | Expected top-three results for each profile using the same dataset |
| Fri, Nov 27 | Add or improve algorithm tests for the manual example and weight profiles | Tests pass locally and cover the documented scenarios |
| Sat, Nov 28 | Verify zero-column, tie, one-room, and all-zero-weight behaviour | A short edge-case note with expected and actual results |
| Sun, Nov 29 | Publish the method work in a pull request | One PR containing only TOPSIS code, tests, and method documentation |

### Trần Khánh Tài — application and integration

| Date | Task | Deliverable |
| --- | --- | --- |
| Mon, Nov 23 | Run the starter application and list the required user flow | A short UI checklist: budget input, five weights, ranking, calculation details, and error states |
| Tue, Nov 24 | Make the input-to-ranking flow clear in the Streamlit application | User can set a budget and five weights, then see a refreshed top-three ranking |
| Wed, Nov 25 | Improve output readability for the top three rooms | Each result clearly shows cost, distance, area, security, amenities, and TOPSIS score |
| Thu, Nov 26 | Show the calculation details needed for the demonstration | Visible normalized weights, D+, D-, C, and an English explanation of the method |
| Fri, Nov 27 | Run the application using the expanded synthetic dataset | A local smoke-check note confirming no UI error occurs with at least 30 rooms |
| Sat, Nov 28 | Prepare the application for a second-computer run | Setup instructions work from a clean clone and virtual environment |
| Sun, Nov 29 | Publish the application work in a pull request | One PR containing only application and integration changes |

### Trần Việt Trung — quality assurance and demo

| Date | Task | Deliverable |
| --- | --- | --- |
| Mon, Nov 23 | Write the Week 1 test checklist | Cases for valid data, invalid data, no match, one match, ties, zero weights, and changed weight profiles |
| Tue, Nov 24 | Test CSV validation with invalid rows | Expected error messages for missing data, duplicates, invalid scores, and invalid numeric values |
| Wed, Nov 25 | Test budget filtering and ranking edge cases | Recorded expected results for no-match, one-match, and tied-room scenarios |
| Thu, Nov 26 | Run the complete automated test suite and log defects | A defect list with reproduction steps and expected behaviour |
| Fri, Nov 27 | Write a five-minute demo script | Budget → weights → top three → calculation details → changed priorities |
| Sat, Nov 28 | Capture offline evidence of the working flow | A screenshot set or short local video plus the exact sample input values used |
| Sun, Nov 29 | Publish testing and demo work in a pull request | One PR containing only tests, the checklist, and demo materials |

## Working rules for the week

1. Each person owns the tasks in their section and directly contacts another member only when they need clarification or a dependency resolved.
2. Make changes in a personal branch and open a pull request into `main`. Do not force-push to `main`.
3. Before pushing, run the checks documented in the root README.
4. Treat the current CSV data as synthetic. Do not add private contact details or unverified real listings.
5. Record changed assumptions, criteria, schema fields, or method choices in the pull request or meeting note.
6. Stop adding features after the Week 1 baseline works. Fix only issues that block the demonstration or produce incorrect rankings.

## Week-end acceptance checklist

- [ ] The team has confirmed the problem, technique, platform, language, criteria, and data approach.
- [ ] At least 30 labelled synthetic room records pass validation.
- [ ] A manual TOPSIS example agrees with the implementation.
- [ ] Users can change budget and weights and receive an updated ranking.
- [ ] No-match, single-match, tied-room, invalid-data, and all-zero-weight scenarios are tested.
- [ ] The application runs on a second computer using the documented setup.
- [ ] The team has saved a screenshot or short offline video of the flow.

## What happens after Week 1

Use the November 29 review to make a realistic Week 2 plan. Only then schedule CSV import/export, sensitivity comparison, richer explanations, report drafting, and slide work. Do not promise a final delivery date for optional features until the Week 1 baseline has been demonstrated.
