# Housing dataset

`rooms_sample.csv` contains thirty **synthetic** rooms for the starter application. The shared dataset already meets the Week 1 expansion target; retain its 30 records and stable IDs. All distances use the same hypothetical campus reference point, called **Demo Campus** in the requirements. These records are not market data or real housing recommendations.

- `id`: unique, nonempty identifier.
- `name`: nonempty room name.
- `monthly_cost_vnd`: rent plus estimated fixed monthly fees, VND, > 0. Cost criterion.
- `distance_km`: distance to campus, km, >= 0. Cost criterion.
- `area_m2`: usable floor area, m², > 0. Benefit criterion.
- `security_score`: integer from 1 to 5, calculated as 1 plus the number of conditions met: private lock, controlled access, common-area cameras, and entrance lighting.
- `amenities_score`: integer from 1 to 5, calculated as 1 plus the number of conditions met: private bathroom, cooking area, Wi-Fi, and parking.
- `source`: exactly `synthetic` for every Week 1 record. This is provenance metadata, not a ranking criterion.

Use UTF-8 CSV files with the eight header fields above and English room labels. All fields are required. Numeric values must be finite; do not use missing values, NaN, infinity, thousands separators, or currency symbols. Use a decimal point for fractions. IDs are unique after trimming surrounding whitespace; the sample uses R01–R30. Names and source must be nonempty after trimming. No imputation is performed: invalid rows cause loading to fail.

Monthly cost is an assumed total of rent and fixed recurring fees for one room per month; no itemized breakdown is available. Deposits and variable consumption are outside this baseline. Distance is an assigned distance in kilometres to the same Demo Campus reference point, not a verified route or travel time. Area is usable room floor area in square metres. Budget filtering includes rooms whose monthly cost is less than or equal to the chosen budget, before ranking. Lower cost and distance are preferred; higher area and both scores are preferred. ID, name, and source are excluded from TOPSIS.

## Security and amenities scoring

Each criterion uses four equally weighted yes/no conditions. Count the conditions met and add one. The conditions are independent: no particular order of features is required.

| Score | Number of conditions met | Interpretation |
| --- | --- | --- |
| 1 | 0 | None of the four conditions |
| 2 | 1 | Any one condition |
| 3 | 2 | Any two conditions |
| 4 | 3 | Any three conditions |
| 5 | 4 | All four conditions |

Security conditions:

1. Private lock: the occupant can lock the individual room.
2. Controlled access: the building entrance restricts entry by key, card, or an attendant.
3. Common-area cameras: cameras cover shared access areas, not private rooms.
4. Entrance lighting: the entrance is illuminated after dark.

Amenities conditions:

1. Private bathroom: a bathroom is reserved for the room's occupants.
2. Cooking area: occupants have access to a designated cooking area.
3. Wi-Fi: internet access is available to the room.
4. Parking: a designated bicycle or motorbike parking area is available.

For example, private lock and entrance lighting yield security 3; private bathroom, cooking area, and Wi-Fi yield amenities 4. A score of 1 is valid and does not mean missing data. Unknown conditions must not silently become absent conditions in any future collected dataset.

The sample contains assigned synthetic aggregate scores only. It does not store feature-level evidence, so individual conditions cannot be reconstructed or independently verified from a score. These rules define the score interpretation; they do not assert that a real property has those features. Security is a feature count, not a measured crime or safety probability. TOPSIS treats one-point score increments numerically as equally spaced; this is a modelling assumption.

## Validation and scope

The application validator is `housing_dss.data.load_rooms`. It checks required columns, nonempty metadata, duplicate IDs, finite nonnegative numeric values, positive cost and area, and integer scores from 1 to 5. The Week 1 audit additionally checks exact column order, no missing cells, 30 records, English sample labels, and `source=synthetic`; these extra conventions are not all enforced by the loader.

See [requirements](../docs/week-1-requirements.md), [validation evidence](../docs/week-1-data-validation.md), and [report input](../docs/week-1-report-input.md). No schema, criteria, directions, or scoring formula changes are introduced by this documentation. Real listings, extra provenance columns, personal data, and private contact details are outside Week 1 scope. Record and agree any later schema or assumption changes before implementation.
