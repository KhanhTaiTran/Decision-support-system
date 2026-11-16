# Housing dataset

`rooms_sample.csv` contains eight **synthetic** rooms for the starter application. An will expand it to 30–50 rooms according to the project plan. All distances use the same hypothetical campus reference point. These records are not market data.

- `id`: unique, nonempty identifier.
- `name`: nonempty room name.
- `monthly_cost_vnd`: rent plus estimated fixed monthly fees, VND, > 0. Cost criterion.
- `distance_km`: distance to campus, km, >= 0. Cost criterion.
- `area_m2`: usable floor area, m², > 0. Benefit criterion.
- `security_score`: integer from 1 to 5, calculated as 1 plus the number of conditions met: private lock, controlled access, common-area cameras, and entrance lighting.
- `amenities_score`: integer from 1 to 5, calculated as 1 plus the number of conditions met: private bathroom, cooking area, Wi-Fi, and parking.
- `source`: `synthetic` for generated records. Real records require a source URL and collection date in additional columns.

Use UTF-8 CSV files and English room labels. Do not commit personal data or private contact details. Clearly identify sources when combining real and synthetic records.
