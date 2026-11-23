# Week 1 data validation

Owner: Hồ Ngọc An. Audit date: November 23, 2026. Dataset: `data/rooms_sample.csv`.

The starter already contains 30 records. This work audits and retains them instead of duplicating the expansion. The checks below were run on the current schema; rerun them if the dataset or schema changes before the November 29 review.

## Reproduce the sample audit

After completing the root README setup, run this from the repository root in PowerShell:

```powershell
@'
import csv
import math
from pathlib import Path
from housing_dss.data import load_rooms

path = Path('data/rooms_sample.csv')
fields = ['id', 'name', 'monthly_cost_vnd', 'distance_km', 'area_m2',
          'security_score', 'amenities_score', 'source']
with path.open(encoding='utf-8', newline='') as handle:
    reader = csv.DictReader(handle)
    assert reader.fieldnames == fields, 'Unexpected header'
    raw = list(reader)
assert len(raw) == 30, 'Expected the 30-room baseline'
assert all(set(row) == set(fields) for row in raw), 'Extra CSV cells'
assert all(row[field] and row[field].strip() for row in raw for field in fields)
assert {row['id'] for row in raw} == {f'R{i:02d}' for i in range(1, 31)}
assert all(row['source'] == 'synthetic' for row in raw)
assert all(row['name'].isascii() for row in raw), 'Review sample labels'
rooms = load_rooms(path)
assert len(rooms) == 30
for field in fields[2:7]:
    values = [room[field] for room in rooms]
    assert all(math.isfinite(value) and value >= 0 for value in values)
    if field in ('monthly_cost_vnd', 'area_m2'):
        assert min(values) > 0
    if field.endswith('_score'):
        assert all(value.is_integer() and 1 <= value <= 5 for value in values)
    print(f'{field}: {min(values):g} to {max(values):g}')
print('PASS: 30 synthetic rooms satisfy the schema and application validator.')
'@ | .\.venv\Scripts\python.exe -
```

ASCII is only a supporting check for these sample labels, not a general English-language detector. The 30 names were also read and checked as English room labels.

## Recorded results

| Check | Result |
| --- | --- |
| UTF-8, eight expected columns, no extra cells | Pass |
| At least 30 records | Pass: exactly 30 |
| Nonempty fields and unique IDs | Pass: R01–R30 |
| English room labels and synthetic sources | Pass: all 30 |
| Finite, nonnegative numbers | Pass |
| Positive monthly cost and area | Pass |
| Integer security and amenities scores in 1–5 | Pass |
| Application `load_rooms` validator | Pass: 30 records loaded |

Observed ranges: monthly cost VND 1,900,000–5,000,000; distance 0.5–7.5 km; area 12–34 m²; security 2–5; amenities 1–5. No missing fields, duplicate IDs, invalid scores, negative values, or zero cost/area were found. No data correction or schema change was required.

## Required repository checks

Run the root README commands after the audit:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m compileall -q app.py src tests
```

Recorded on November 23, 2026, using Python 3.14 on Windows: all 9 unit tests passed; `compileall` completed successfully. The first sandboxed test run could not write a temporary test file; rerunning with temporary-directory access passed without code changes.

These checks validate the repository in the current environment. They do not establish team meeting approval, a manual TOPSIS comparison, or a run on a second computer.
