# Chapter 3. Requirements and Scoring Rubric

Author: Hồ Ngọc An · Draft: 2026-11-26

This chapter specifies what the Student Housing DSS must do (functional requirements), how well it must do it (non-functional requirements), the data it uses, and the rubric used to score security and amenities. Each requirement has an identifier so that it can be traced to the implementation (Chapter 5) and to the tests (Chapter 6).

## 3.1 Stakeholders and Users

| Stakeholder | Role | Main interest |
| --- | --- | --- |
| Student (primary user) | Enters budget and priorities, reads the ranking | A short, trustworthy list of rooms that fit their needs |
| Project team | Builds and maintains the system | Correct algorithm, clean data, working demo |
| Lecturer / evaluator | Assesses the project | Sound method, explainable results, verified correctness |

Landlords and listing websites are not users of the system in the current scope.

## 3.2 User Stories

| ID | User story | Acceptance criteria |
| --- | --- | --- |
| US-01 | As a student, I want to enter my maximum monthly budget so that I only see rooms I can afford. | Rooms with a monthly cost above the budget never appear in the results. |
| US-02 | As a student, I want to set how important each of the five criteria is to me so that the ranking reflects my priorities. | Five sliders (0–100); changing a slider updates the ranking. |
| US-03 | As a student, I want to choose a ready-made priority profile so that I can get a ranking quickly without tuning every slider. | One click on a preset sets all five sliders to the profile's values. |
| US-04 | As a student, I want to see the top three rooms with their values and score so that I can shortlist rooms to visit. | Up to three rooms shown with ID, name, five criterion values, and TOPSIS score. |
| US-05 | As a student, I want to see how the score was calculated so that I can trust and explain the result. | Normalised weights and $D^+$, $D^-$, $C$ for each room are displayed. |
| US-06 | As a student, I want to change my priorities and immediately see how the ranking changes so that I understand the trade-offs. | The result is recalculated after every change, without reloading the page. |
| US-07 | As a student, I want to upload my own list of rooms and download the ranked result so that I can use the tool with rooms I found myself. | A valid CSV can be uploaded and the ranked table downloaded as CSV. |

## 3.3 Main Use Case: Rank Rooms

| Item | Description |
| --- | --- |
| Actor | Student |
| Precondition | The application is running and a valid room dataset is available. |
| Main flow | 1. The student enters a maximum budget. 2. The student selects a preset profile or adjusts the five weight sliders. 3. The system loads and validates the dataset. 4. The system removes rooms above the budget. 5. The system ranks the remaining rooms with TOPSIS. 6. The system shows the top three, all eligible rooms, and calculation details. 7. The student changes weights or budget; the system repeats steps 4–6. |
| Alternative flow A | No room is within the budget: the system shows a message suggesting a higher budget. |
| Alternative flow B | Only one room is within the budget: the system shows it and states that there is nothing to compare. |
| Exception E1 | All weights are zero: the system shows an error and does not rank. |
| Exception E2 | The dataset is invalid (missing column, duplicate ID, out-of-range value): the system shows an error that names the problem and the row. |
| Postcondition | The student has a ranked shortlist and an explanation of the ranking. |

## 3.4 Functional Requirements

Status reflects the repository on 26 November 2026 and must be updated before submission.

| ID | Requirement | Related story | Status |
| --- | --- | --- | --- |
| FR-01 | The system shall load room data from a UTF-8 CSV file that follows the schema in Section 3.6. | – | Implemented |
| FR-02 | The system shall reject an invalid dataset before ranking and display an error message identifying the row and the problem. | – | Implemented |
| FR-03 | The system shall let the user enter a maximum monthly budget in VND (≥ 0). | US-01 | Implemented |
| FR-04 | The system shall exclude rooms whose monthly cost exceeds the budget before ranking (hard constraint, inclusive: cost ≤ budget is kept). | US-01 | Implemented |
| FR-05 | The system shall provide one weight control (0–100) for each of the five criteria. | US-02 | Implemented |
| FR-06 | The system shall normalise the weights so that they sum to 1, and reject a set of weights whose total is 0. | US-02 | Implemented |
| FR-07 | The system shall provide four preset weight profiles: Balanced, Budget-First, Campus-Proximity, and Comfort & Space. | US-03 | Implemented |
| FR-08 | The system shall rank eligible rooms using vector-normalised TOPSIS, treating cost and distance as cost criteria and area, security, and amenities as benefit criteria. | US-02 | Implemented |
| FR-09 | The system shall display the top three eligible rooms (or fewer if fewer are eligible) with ID, name, five criterion values, and TOPSIS score. | US-04 | Implemented |
| FR-10 | The system shall display the complete ranking of all eligible rooms. | US-04 | Implemented |
| FR-11 | The system shall display the normalised weights and the values $D^+$, $D^-$, and $C$ for every eligible room. | US-05 | Implemented |
| FR-12 | The system shall recalculate and redisplay the ranking whenever the budget or a weight changes. | US-06 | Implemented |
| FR-13 | The system shall order rooms with equal scores by ID so that the ranking is deterministic. | – | Implemented |
| FR-14 | The system shall display a clear message when no room, or only one room, is within the budget. | – | Implemented |
| FR-15 | The system shall allow the user to upload a custom CSV file of rooms that follows the same schema. | US-07 | Planned (Phase 1) |
| FR-16 | The system shall allow the user to download the ranked results, including scores, as a CSV file. | US-07 | Planned (Phase 1) |

## 3.5 Non-functional Requirements

| ID | Category | Requirement | How it is checked |
| --- | --- | --- | --- |
| NFR-01 | Performance | For a dataset of up to 100 rooms, the ranking shall update within 1 second after a change on a standard laptop. | Manual timing during the demo |
| NFR-02 | Usability | A first-time user shall be able to obtain a top-three ranking within 1 minute without instructions. | Walk-through with a classmate |
| NFR-03 | Explainability | Every displayed score shall be traceable to its $D^+$ and $D^-$ values in the calculation details. | Inspection of the interface |
| NFR-04 | Correctness | The software ranking and scores for a three-room example shall match a manual calculation within the documented rounding (4 decimal places). | Automated test against Chapter 4 example |
| NFR-05 | Reliability | The application shall not crash on an empty result, a single eligible room, all-zero weights, or an invalid CSV file. | Automated edge-case tests |
| NFR-06 | Portability | The application shall run locally on Windows, macOS, and Linux with Python 3.11+ by following the README only. | Setup on a second computer |
| NFR-07 | Language | All interface text, messages, code identifiers, and documentation shall be in English. | Code and document review |
| NFR-08 | Privacy | The system shall not collect, store, or transmit personal data; the dataset shall contain no personal contact details. | Data and code review |
| NFR-09 | Maintainability | The TOPSIS module shall be independent of the user interface and file access, and the five criterion column names shall not change. | Code review; module structure |
| NFR-10 | Academic integrity | Synthetic data shall be labelled `synthetic` and shall not be presented as real market data. | Data validation check |

## 3.6 Data Requirements

### 3.6.1 Data dictionary

| Column | Type | Unit | Rule | TOPSIS role |
| --- | --- | --- | --- | --- |
| `id` | Text | – | Unique, nonempty | Not used |
| `name` | Text | – | Nonempty English label | Not used |
| `monthly_cost_vnd` | Number | VND / month | > 0; rent plus estimated fixed fees | Cost |
| `distance_km` | Number | km | ≥ 0; distance to the campus reference point | Cost |
| `area_m2` | Number | m² | > 0; usable floor area | Benefit |
| `security_score` | Integer | 1–5 | Security rubric (Section 3.7) | Benefit |
| `amenities_score` | Integer | 1–5 | Amenities rubric (Section 3.7) | Benefit |
| `source` | Text | – | `synthetic` for generated records | Not used |

File rules: UTF-8 CSV with a header row, decimal point for fractions, no thousands separators or currency symbols, and no empty cells. Deposits and variable utility use are not included in the monthly cost.

### 3.6.2 Baseline dataset

The baseline dataset `data/rooms_sample.csv` contains **30 synthetic rooms** (`R01`–`R30`). The values were chosen to be plausible for student rooms near VNU-HCM International University, but they are not real listings.

| Criterion | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- |
| Monthly cost (VND) | 1,900,000 | 5,000,000 | 3,253,333 | 3,150,000 |
| Distance (km) | 0.5 | 7.5 | 3.16 | 2.75 |
| Area (m²) | 12 | 34 | 22.4 | 22.5 |
| Security score | 2 | 5 | 3.60 | 4 |
| Amenities score | 1 | 5 | 3.57 | 4 |

### 3.6.3 Data validation

The validator `load_rooms` rejects a file when a required column is missing, an ID/name/source is empty, an ID is duplicated, a criterion is non-numeric, negative, or infinite, cost or area is zero, or a score is not an integer from 1 to 5. The baseline dataset was checked on 26 November 2026 and passed all checks: 30 rows, IDs `R01`–`R30` with no duplicates, unique English names, all sources `synthetic`, and all values within range (details in `docs/data-validation.md`).

Four rooms are dominated, meaning another room is equal or better on all five criteria: R15 (by R03), R23 (by R06), R22 (by R07), and R10 (by R08). This is not an error; it gives a simple consistency check for the ranking, because a dominated room should not be ranked above the room that dominates it.

## 3.7 Scoring Rubric for Security and Amenities

Cost, distance, and area are measured directly. Security and amenities are qualitative, so the project defines a rubric that turns them into comparable 1–5 scores. The rubric is designed to be **objective** (each condition is a yes/no check), **simple** (four conditions per criterion), and **repeatable** (two people checking the same room obtain the same score).

### 3.7.1 Formula

$$\text{score} = 1 + \text{number of conditions met (out of 4)}$$

| Conditions met | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| Score | 1 | 2 | 3 | 4 | 5 |

All conditions have equal weight, and the order in which they are met does not matter.

### 3.7.2 Security conditions

| # | Condition | Counts as met when |
| --- | --- | --- |
| S1 | Private door lock | The occupant can lock their own room with a key or code that only they hold. |
| S2 | Access control or guard | Entry to the building is restricted by a gate key, access card, fingerprint, or an on-site guard/landlord. |
| S3 | Security cameras | Cameras cover the entrance, corridors, or parking area (never inside private rooms). |
| S4 | Walkway lighting | The entrance, corridors, and path to the room are lit at night. |

### 3.7.3 Amenities conditions

| # | Condition | Counts as met when |
| --- | --- | --- |
| A1 | Private bathroom | The room has its own toilet and shower, not shared with other rooms. |
| A2 | Cooking area | Occupants may cook in the room or in a designated shared kitchen. |
| A3 | Wi-Fi | Internet is available in the room, included or for a fixed fee. |
| A4 | Safe motorbike parking | A designated, covered or supervised parking area for motorbikes is available. |

### 3.7.4 Worked examples

| Room features | Calculation | Score |
| --- | --- | --- |
| S1, S4 | 1 + 2 | Security = 3 |
| S1, S2, S3, S4 | 1 + 4 | Security = 5 |
| A1, A2, A3 | 1 + 3 | Amenities = 4 |
| A3 only | 1 + 1 | Amenities = 2 |

### 3.7.5 Score distribution in the baseline dataset

| Score | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Security (rooms) | 0 | 4 | 10 | 10 | 6 |
| Amenities (rooms) | 1 | 5 | 7 | 10 | 7 |

### 3.7.6 Rubric limitations

- A score of 1 is a valid value (no conditions met), not missing data. When real data is collected, an unknown condition must be recorded as unknown, not counted as "not met".
- The baseline dataset stores only final scores, not the individual conditions. The rubric explains what a score means but does not prove that a real property has those features.
- The security score counts protective features; it is not a measure of crime rate or actual safety.
- TOPSIS treats each one-point step as equal in size, which is a modelling assumption.

## 3.8 Requirements Traceability

| Requirement | Implementation | Verification |
| --- | --- | --- |
| FR-01, FR-02 | `src/housing_dss/data.py` (`load_rooms`) | `tests/test_data.py` |
| FR-03 – FR-07 | `src/housing_dss/ui/preferences.py`, `src/housing_dss/criteria.py` | `tests/test_ui.py` |
| FR-08, FR-13 | `src/housing_dss/topsis.py` (`rank_rooms`) | `tests/test_topsis.py` |
| FR-09 – FR-12, FR-14 | `src/housing_dss/ui/results.py`, `app.py` | `tests/test_ui.py`, demo walk-through |
| FR-15, FR-16 | Planned | Planned |
| NFR-04 | `src/housing_dss/topsis.py` | Manual example (Chapter 4) and test (Chapter 6) |
| NFR-05 | `data.py`, `topsis.py`, `results.py` | Edge-case tests (Chapter 6) |
| NFR-10 | `data/rooms_sample.csv`, `data/README.md` | `tests/test_data.py`, `docs/data-validation.md` |

## 3.9 Summary

The system's requirements centre on one main use case: a student sets a budget and priorities and receives an explainable TOPSIS ranking of affordable rooms. Sixteen functional and ten non-functional requirements define this behaviour, and a 30-room synthetic dataset with a validated schema supports it. The yes/no scoring rubric makes security and amenities comparable and repeatable. Chapter 4 uses this data to present the TOPSIS model in detail.
