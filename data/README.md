# Housing dataset

`rooms_sample.csv` contains thirty **synthetic** rooms (`R01`–`R30`) used by the application. The values were generated to be plausible for student rooms near VNU-HCM International University, but they are **not market data** and must not be presented as real listings. All distances use the same hypothetical campus reference point.

## Data dictionary

| Column | Type | Unit | Rule | TOPSIS role |
| --- | --- | --- | --- | --- |
| `id` | Text | – | Unique, nonempty. The sample uses `R01`–`R30`. | Not used |
| `name` | Text | – | Nonempty English room label. | Not used |
| `monthly_cost_vnd` | Number | VND / month | > 0. Rent plus estimated fixed monthly fees. | Cost (lower is better) |
| `distance_km` | Number | km | >= 0. Distance to the campus reference point. | Cost (lower is better) |
| `area_m2` | Number | m² | > 0. Usable floor area of the room. | Benefit (higher is better) |
| `security_score` | Integer | 1–5 | Calculated with the security rubric below. | Benefit (higher is better) |
| `amenities_score` | Integer | 1–5 | Calculated with the amenities rubric below. | Benefit (higher is better) |
| `source` | Text | – | `synthetic` for generated records. Real records need a source URL and collection date in extra columns. | Not used |

File format: UTF-8 CSV, one header row, decimal point for fractions, no thousands separators or currency symbols, no empty cells. Do not rename the five criterion columns; the application and tests depend on them.

Deposits and variable utility use (electricity, water by meter) are not included in `monthly_cost_vnd`. Distance is an assigned value, not a measured route or travel time.

## Scoring rubric for security and amenities

Both scores use the same formula:

```text
score = 1 + number of conditions met (out of 4)
```

Each condition is a yes/no check with equal weight, so the score is always an integer from 1 to 5.

| Conditions met | Score | Meaning |
| --- | --- | --- |
| 0 | 1 | None of the four conditions |
| 1 | 2 | Any one condition |
| 2 | 3 | Any two conditions |
| 3 | 4 | Any three conditions |
| 4 | 5 | All four conditions |

### Security conditions

| # | Condition | Counts as met when |
| --- | --- | --- |
| 1 | Private door lock | The occupant can lock their own room with a key or code that only they hold. |
| 2 | Access control or guard | Entry to the building is restricted by a gate key, access card, fingerprint, or an on-site guard/landlord. |
| 3 | Security cameras | Cameras cover the entrance, corridors, or parking area (never inside private rooms). |
| 4 | Walkway lighting | The entrance, corridors, and path to the room are lit at night. |

### Amenities conditions

| # | Condition | Counts as met when |
| --- | --- | --- |
| 1 | Private bathroom | The room has its own toilet and shower, not shared with other rooms. |
| 2 | Cooking area | Occupants may cook in the room or in a designated shared kitchen. |
| 3 | Wi-Fi | Internet is available in the room, included or for a fixed fee. |
| 4 | Safe motorbike parking | A designated, covered or supervised parking area for motorbikes is available. |

### Examples

| Features present | Calculation | Score |
| --- | --- | --- |
| Private lock, walkway lighting | 1 + 2 | Security = 3 |
| Private lock, access control, cameras, walkway lighting | 1 + 4 | Security = 5 |
| Private bathroom, cooking area, Wi-Fi | 1 + 3 | Amenities = 4 |
| Wi-Fi only | 1 + 1 | Amenities = 2 |

### Notes and limitations

- A score of 1 is a valid value (no conditions met), not missing data.
- An unknown condition must not be counted as "not met" when real data is collected; record it as unknown and resolve it before scoring.
- The sample stores only the final scores, not the individual conditions. The rubric explains what each score means; it does not claim that a real property has those features.
- The security score is a count of protective features, not a measured crime rate or safety probability.
- TOPSIS treats each one-point step as equal in size. This is a modelling assumption.

## Validation

`housing_dss.data.load_rooms` rejects files with missing columns, empty ID/name/source, duplicate IDs, non-numeric or negative values, zero cost or area, and scores that are not integers from 1 to 5. The latest dataset check is in [docs/data-validation.md](../docs/data-validation.md).

Do not commit personal data or private contact details. When combining real and synthetic records, identify the source of every row.
