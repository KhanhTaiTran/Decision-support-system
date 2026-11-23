# Week 1 requirements — student housing selection

Owner: Hồ Ngọc An. Prepared November 23, 2026, for the November 23–29 baseline.

## Problem and users

Students choosing a room near a campus must balance affordability, distance, space, security features, and amenities. The baseline supports a student comparing synthetic room alternatives around one hypothetical reference point, **Demo Campus**. It helps make trade-offs visible; it does not select or book housing on the student's behalf. Demo Campus names the existing hypothetical reference point and does not identify a real institution or a verified geographic area.

## Baseline decisions and confirmation status

Use the repository's proposed decisions: a model-driven DSS using TOPSIS, implemented as a local Python + Streamlit web application, with English interface and project materials and clearly labelled synthetic data. No replacement method or platform is proposed. These are the working assumptions for this deliverable; team meeting confirmation has not been supplied and is still pending. Record confirmation or a replacement in the meeting note or PR before changing code.

| Criterion | Unit | Preference |
| --- | --- | --- |
| Total monthly cost | VND/month | Lower is better |
| Distance to Demo Campus | km | Lower is better |
| Usable floor area | m² | Higher is better |
| Security feature score | Integer 1–5 | Higher is better |
| Amenities feature score | Integer 1–5 | Higher is better |

The [data dictionary](../data/README.md) defines fields, score rules, and assumptions.

## Required flow and acceptance conditions

1. Load at least 30 synthetic rooms from the bundled UTF-8 CSV. Reject invalid records with a useful error before ranking.
2. Let a student choose a maximum monthly budget and nonnegative priorities for the five criteria. At least one priority must be positive.
3. Keep rooms at or below the budget, then rank eligible rooms with TOPSIS using the stated cost/benefit directions.
4. Display up to three leading rooms with their criterion values and score, plus calculation details explaining the trade-offs. Changing budget or priorities must update the result.
5. Handle no eligible rooms, one eligible room, tied alternatives, invalid data, and all-zero weights through documented behaviour and tests.
6. Support a local run from the README setup and a second-computer demonstration. The manual TOPSIS comparison and demo evidence belong to the other owners in the [Week 1 plan](week-1-plan.md).

## Boundaries and handoff

This contribution supplies requirements, the data dictionary, an audit of the existing 30-room sample, and report input. It does not claim team approval, a second-computer run, or completion of other owners' acceptance checks. Login, maps, scraping, payment, machine learning, CSV import/export, and optional features are deferred. Use the November 29 review to decide Week 2 scope. No final delivery date is assigned to optional work.
