# Dataset validation: `data/rooms_sample.csv`

Owner: Hồ Ngọc An · Checked: 2026-11-26 · Dataset: 30 synthetic rooms

## Checklist

| Check | Result |
| --- | --- |
| File loads through `housing_dss.data.load_rooms` (schema, numeric values, ranges) | Pass |
| Exactly 30 rows | Pass |
| IDs are `R01` to `R30`, in order, no duplicates | Pass |
| Room names are unique, nonempty, English | Pass |
| Every `source` value is `synthetic` | Pass |
| No missing fields | Pass |
| `monthly_cost_vnd` > 0 and `area_m2` > 0 | Pass |
| `distance_km` >= 0 | Pass |
| `security_score` and `amenities_score` are integers from 1 to 5 | Pass |
| UTF-8 encoding, no BOM | Pass |

## Value ranges

| Criterion | Type | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- |
| `monthly_cost_vnd` | Cost | 1,900,000 | 5,000,000 | 3,253,333 | 3,150,000 |
| `distance_km` | Cost | 0.5 | 7.5 | 3.16 | 2.75 |
| `area_m2` | Benefit | 12 | 34 | 22.4 | 22.5 |
| `security_score` | Benefit | 2 | 5 | 3.60 | 4 |
| `amenities_score` | Benefit | 1 | 5 | 3.57 | 4 |

Rent per square metre ranges from about 117,000 to 191,000 VND/m².

Score distribution:

- Security: 2 → 4 rooms, 3 → 10, 4 → 10, 5 → 6 (no room scores 1).
- Amenities: 1 → 1 room, 2 → 5, 3 → 7, 4 → 10, 5 → 7.

## Observations

- **Plausibility.** Rents of 1.9–5.0 million VND per month for 12–34 m² rooms within 7.5 km of campus are in a plausible range for student rooms around VNU-HCM (Thủ Đức / Dĩ An). This is a judgement for synthetic data, not a market survey. The values must not be presented as real market prices.
- **Dominated rooms.** Four rooms are equal or worse than another room on all five criteria: R15 (by R03), R23 (by R06), R22 (by R07), and R10 (by R08). This is not a data error. These rooms can never outrank the room that dominates them, which is useful when explaining TOPSIS results.
- **Distance reference.** All distances use one hypothetical campus reference point, as stated in `data/README.md`.

## How to re-run

```powershell
.\.venv\Scripts\python.exe -m unittest tests.test_data -v
```
