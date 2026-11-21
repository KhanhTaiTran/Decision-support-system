# Week 1 plan: November 21–27, 2026

## Week objective

Finish and validate one complete decision-support flow that the whole team can run locally:

```text
Synthetic room data → validation → budget filter → TOPSIS ranking → top-three explanation → tests
```

This is a working baseline, not the final application. The team should avoid login, maps, scraping, payment, machine learning, and other optional features during this week.

## Decisions to confirm at the first meeting

The proposed answers are already reflected in the starter repository. The team should either confirm them or record a replacement by November 22.

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

## Day-by-day work

| Date | Team outcome | Owner | Concrete output |
| --- | --- | --- | --- |
| Sat, Nov 21 | Everyone can access the repository and run the starter | Tài coordinates; all members verify | Each member clones the repo, runs the tests and application, and reports one blocker or `ready` |
| Sun, Nov 22 | Scope and data rules are agreed | An leads; all review | One decision record covering the eight questions above; final data schema and criterion definitions approved |
| Mon, Nov 23 | Ranking method is independently verified | Phát leads; Trung reviews | A three-room, hand-calculated TOPSIS example with matrix, normalized weights, ideal solutions, D+, D-, C, and expected ranking |
| Tue, Nov 24 | Dataset and UI input path are usable | An and Tài | 30 labelled synthetic rooms; budget and weight controls work with the agreed schema |
| Wed, Nov 25 | The system explains and tests the ranking | Phát and Trung | Test cases for no matches, one match, ties, zero weights, invalid rows, and different weight profiles; top-three explanation is visible |
| Thu, Nov 26 | First team review is completed | Trung leads; all review | Short defect list with priority and owner; only demo-blocking issues enter the fix list |
| Fri, Nov 27 | Week 1 baseline is demonstrated | Tài runs; all participate | Five-minute local demo on a second computer, passing automated tests, screenshot/video evidence, and a short retrospective |

## Provisional ownership

These assignments are only a starting point. Rebalance them in the first meeting if someone has stronger experience in another area.

| Member | Week 1 responsibility | Definition of done |
| --- | --- | --- |
| Hồ Ngọc An | Requirements and data | Data dictionary is complete; 30 synthetic records are valid and source-labelled |
| Châu Thành Phát | TOPSIS method | Manual example matches the code; criterion directions and weight normalization are documented |
| Trần Khánh Tài | App integration | A clean local Streamlit flow works from inputs to top-three results on a second computer |
| Trần Việt Trung | Quality and demo | Test checklist is complete; automated tests pass; one five-minute demo script is ready |

## Working rules for the week

1. Use a short daily check-in: completed work, next task, blocker. Keep it under 10 minutes.
2. Make changes in a personal branch and open a pull request into `main`. Do not force-push to `main`.
3. Before pushing, run the checks documented in the root README.
4. Treat the current CSV data as synthetic. Do not add private contact details or unverified real listings.
5. Record changed assumptions, criteria, schema fields, or method choices in the pull request or meeting note.
6. Stop adding features after the Friday baseline works. Fix only issues that block the demonstration or produce incorrect rankings.

## Friday acceptance checklist

- [ ] The team has confirmed the problem, technique, platform, language, criteria, and data approach.
- [ ] At least 30 labelled synthetic room records pass validation.
- [ ] A manual TOPSIS example agrees with the implementation.
- [ ] Users can change budget and weights and receive an updated ranking.
- [ ] No-match, single-match, tied-room, invalid-data, and all-zero-weight scenarios are tested.
- [ ] The application runs on a second computer using the documented setup.
- [ ] The team has saved a screenshot or short offline video of the flow.

## What happens after Week 1

Use the Friday review to make a realistic Week 2 plan. Only then schedule CSV import/export, sensitivity comparison, richer explanations, report drafting, and slide work. Do not promise a final delivery date for optional features until the Week 1 baseline has been demonstrated.
