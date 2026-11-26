# Chapter 1. Problem Statement and Scope

Author: Hồ Ngọc An · Draft: 2026-11-26

## 1.1 Background

Every academic year, many students move away from home to study and must find a room to rent near their university. For students at International University (VNU-HCM), the surrounding area of Thủ Đức and Dĩ An offers a large number of rental rooms that differ in price, location, size, safety, and facilities. Choosing among them is usually done informally: students browse listings, ask friends, visit a few rooms, and decide based on intuition.

This decision matters. Rent is often the largest monthly expense for a student, distance determines daily travel time and cost, and the quality of a room affects study conditions, safety, and well-being for at least a semester. A poor choice is costly to reverse because moving again requires a new deposit, time, and effort.

<!-- TODO: add one or two cited figures (e.g. number of students in VNU-HCM dormitory vs. renting, typical rent range) with sources before final submission. Do not use the synthetic dataset as evidence of market prices. -->

## 1.2 Problem Statement

Selecting a rental room is a **multi-criteria decision problem**. The criteria conflict with each other:

- A cheaper room is often farther from campus or smaller.
- A room close to campus with good facilities usually costs more.
- Security and amenities are hard to compare across listings because they are described in different, informal ways.

When students compare rooms one criterion at a time, or rely on a general impression, three problems appear:

1. **Trade-offs are not made explicit.** It is unclear how much extra rent a student is willing to accept for a shorter distance or a larger room.
2. **Comparison is inconsistent.** Different rooms are judged with different standards, and qualitative features (security, amenities) are not measured in a common way.
3. **Decisions are hard to explain or repeat.** If preferences change, for example when the budget is reduced, the student must redo the whole comparison mentally.

The problem addressed by this project is therefore:

> How can a student systematically compare available rooms on several conflicting criteria, according to their own budget and priorities, and obtain a ranked shortlist that is transparent and easy to explain?

## 1.3 Target Users and Decision Context

The primary user is a **university student looking for a rental room near campus**. The student:

- has a maximum monthly budget that cannot be exceeded;
- cares about several factors at once, but with different personal priorities (for example, one student values low cost most, another values being close to campus);
- is not expected to know any decision-making method or mathematics.

The decision is **semi-structured**: the criteria and data can be modelled, but the final choice still depends on the student's judgement (for example, after visiting the room). The system therefore **supports** the decision rather than making it. It produces a ranked shortlist and explains the ranking; it does not book, reserve, or recommend a single "correct" room.

## 1.4 Objectives

The project builds a **model-driven Decision Support System (DSS)** for student housing selection. Its objectives are:

1. **Model the decision** using five measurable criteria: total monthly cost, distance to campus, floor area, security score, and amenities score.
2. **Standardise qualitative criteria** with an explicit 1–5 scoring rubric, so that security and amenities are scored consistently (see Chapter 3).
3. **Respect the budget as a hard constraint**: rooms above the student's budget are excluded before ranking.
4. **Rank the remaining rooms with TOPSIS**, using weights that the student sets directly or through preset profiles.
5. **Make the result explainable** by showing the top three rooms, the full ranking, and the intermediate values of the calculation (distances to the ideal and anti-ideal solutions and the closeness score).
6. **Let students explore trade-offs** by changing weights and immediately seeing how the ranking changes (sensitivity analysis).
7. **Verify correctness** by comparing the software output with a manually calculated example and by automated tests.

## 1.5 Scope

### In scope

| Area | Included |
| --- | --- |
| Decision model | Five criteria, cost/benefit directions, user-defined weights, TOPSIS with vector normalisation |
| Data | A dataset of 30 synthetic rooms with a documented data dictionary and scoring rubric |
| Constraint | Hard budget filter applied before ranking |
| Application | Local web application built with Python and Streamlit, English interface |
| User interaction | Budget input, five weight sliders, preset weight profiles, top-three display, full ranking, calculation details |
| Data exchange | Uploading a custom CSV file and downloading the ranked results (planned in Phase 1) |
| Quality | Manual TOPSIS benchmark, automated unit tests, edge-case handling (no eligible room, all-zero weights, invalid file) |

### Optional extensions (Phase 2, only if Phase 1 is complete)

- Collecting real rental listings from public websites around VNU-HCM.
- An interactive map showing the campus and the ranked rooms.
- Charts (radar or bar) comparing the top three rooms across criteria.

These extensions are not required for the system to meet its objectives. If they are not completed, they are discussed as future work in Chapter 7.

### Out of scope

- User accounts, login, and storage of personal data.
- Booking, payment, or contact with landlords.
- Verifying that a listing is real, available, or accurately described.
- Measuring actual safety or crime levels; the security score is a feature count, not a risk measure.
- Machine-learning recommendation or prediction of student satisfaction.

## 1.6 Decision Criteria Overview

| Criterion | Unit | Direction | Why it matters |
| --- | --- | --- | --- |
| Total monthly cost | VND / month | Lower is better | Main financial constraint for students |
| Distance to campus | km | Lower is better | Daily travel time and transport cost |
| Floor area | m² | Higher is better | Living and study space |
| Security score | 1–5 | Higher is better | Personal safety and protection of belongings |
| Amenities score | 1–5 | Higher is better | Daily comfort and convenience |

The exact definitions, data rules, and the scoring rubric for security and amenities are presented in Chapter 3. The TOPSIS method is presented in Chapters 2 and 4.

## 1.7 Assumptions and Limitations

- **Synthetic data.** The baseline dataset contains 30 synthetic rooms (`R01`–`R30`) with values chosen to be plausible for the area around VNU-HCM. They are used for demonstration and testing and do not represent real listings or market prices.
- **Single reference point.** All distances are measured to one campus reference point. Travel time, routes, and transport mode are not modelled.
- **Cost definition.** Monthly cost includes rent and estimated fixed fees. Deposits and variable utility use are excluded.
- **Scores are aggregate.** Security and amenities are stored as final 1–5 scores, not as individual features, and each one-point step is treated as equal in size.
- **Relative ranking.** A TOPSIS score shows how close a room is to the best option *within the current set of eligible rooms*. It is not a probability of suitability, and adding or removing rooms can change the ranking.
- **Budget only as a hard constraint.** Other preferences are expressed as weights; the system does not support additional hard filters (for example, "must have a private bathroom").

## 1.8 Structure of the Report

- **Chapter 1** introduces the problem, users, objectives, and scope.
- **Chapter 2** presents the theoretical background of model-driven DSS and multi-criteria decision making.
- **Chapter 3** describes the requirements, the dataset, and the scoring rubric.
- **Chapter 4** explains the TOPSIS model and a manually calculated three-room example.
- **Chapter 5** describes the system architecture and user interface.
- **Chapter 6** reports testing and sensitivity analysis.
- **Chapter 7** discusses limitations and future work.
- **Chapter 8** concludes the report.
