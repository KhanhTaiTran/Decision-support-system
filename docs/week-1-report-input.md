# Report input — problem, user needs, and data

Prepared by Hồ Ngọc An's requirements/data workstream on November 23, 2026. Draft for reuse in the report; team confirmation of the proposed decisions remains pending.

## Problem statement

Housing selection involves competing objectives. A cheaper room may be farther from campus or offer less space, while a room with more amenities may exceed a student's budget. Comparing one criterion at a time does not express these trade-offs consistently. The project provides a model-driven decision support system that filters unaffordable rooms and uses TOPSIS to compare the remaining alternatives according to student-defined priorities.

## User needs and objectives

The target user is a student comparing rooms around a single campus reference point. The student needs to set a monthly spending limit, express the relative importance of five criteria, inspect the leading alternatives, and understand why preferences affect the ranking. The baseline aims to make this process repeatable and explainable in a local English-language Python + Streamlit application. It supports judgement; a TOPSIS score is not a probability of suitability or a guarantee of housing quality.

## Dataset description

The existing `data/rooms_sample.csv` provides 30 synthetic alternatives, R01–R30, with English names and `synthetic` in every source field. This already satisfies the planned expansion from eight to at least 30 records; no additional rows are needed for this contribution. Each record has eight fields: three metadata fields and five numeric criteria. Monthly cost and distance are cost criteria; usable area, security, and amenities are benefit criteria.

The sample spans VND 1,900,000–5,000,000 per month, 0.5–7.5 km from the hypothetical Demo Campus reference point, and 12–34 m². Security scores span 2–5 and amenities scores 1–5. These ranges describe this synthetic sample only and are not estimates of a real housing market. The schema permits security score 1 even though this sample has none.

## Assumptions and limitations

- Each row represents one comparable room alternative. All distances refer to the same hypothetical campus; no real campus, travel-time model, or route is asserted.
- Cost is an assigned monthly total including estimated fixed fees, without itemized components. Deposits and variable consumption are excluded.
- Security and amenities use one plus the number of four conditions met, as defined in the [dictionary](../data/README.md). The CSV stores synthetic aggregate scores, without feature evidence. Equal numerical score steps are a modelling assumption, not a measured utility scale.
- The budget is a hard inclusive filter. Other preferences are weights in the ranking, not hard constraints. The ranking depends on the eligible candidate set and selected weights.
- Synthetic data supports demonstration and validation, not claims about actual availability, prices, safety, or student satisfaction. No private contact details or unverified real listings are included.
- The existing schema, criterion directions, TOPSIS choice, and scoring formulas are retained. Team agreement must be recorded separately; this draft does not constitute meeting minutes.

## Evidence and remaining team work

The [data audit](week-1-data-validation.md) records the sample checks and application-validator result. The [requirements note](week-1-requirements.md) describes the intended flow. Method verification, complete demo evidence, and a second-computer run remain with their respective Week 1 owners. These results should be added to the final report only after they have been obtained.
