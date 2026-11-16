"""CSV boundary: validate once before passing records to the ranking model."""

import csv
import math
from pathlib import Path
from .criteria import CRITERIA

REQUIRED_FIELDS = {"id", "name", "source", *CRITERIA}


def load_rooms(path: str | Path) -> list[dict]:
    with open(path, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not REQUIRED_FIELDS.issubset(reader.fieldnames or []):
            raise ValueError("CSV columns are missing. See the schema in data/README.md.")
        rooms, seen = [], set()
        for line, row in enumerate(reader, start=2):
            record = {key: (row.get(key) or "").strip() for key in REQUIRED_FIELDS}
            if not all(record[key] for key in ("id", "name", "source")):
                raise ValueError(f"Row {line}: ID, name, or source is missing.")
            if record["id"] in seen:
                raise ValueError(f"Row {line}: duplicate ID.")
            seen.add(record["id"])
            for key in CRITERIA:
                try:
                    value = float(record[key])
                except ValueError as error:
                    raise ValueError(f"Row {line}: {key} must be numeric.") from error
                if not math.isfinite(value) or value < 0:
                    raise ValueError(f"Row {line}: {key} must be finite and nonnegative.")
                if key in ("monthly_cost_vnd", "area_m2") and value == 0:
                    raise ValueError(f"Row {line}: {key} must be greater than 0.")
                if key.endswith("_score") and (not 1 <= value <= 5 or not value.is_integer()):
                    raise ValueError(f"Row {line}: {key} must be an integer from 1 to 5.")
                record[key] = value
            rooms.append(record)
        return rooms
