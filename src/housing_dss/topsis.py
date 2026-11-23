"""Vector-normalized TOPSIS. No UI or file access in this module."""

import math
from collections.abc import Mapping
from .criteria import CRITERIA

def rank_rooms(rooms: list[dict], weights: Mapping[str, float]) -> list[dict]:
    keys = list(CRITERIA)
    if set(weights) != set(keys):
        raise ValueError("Provide weights for exactly the five supported criteria.")
    weight_values = [float(weights[key]) for key in keys]
    if any(not math.isfinite(w) or w < 0 for w in weight_values) or sum(weight_values) == 0:
        raise ValueError("Weights must be nonnegative and finite, with a positive total.")
    if not rooms:
        return []
    matrix = [[float(room[key]) for key in keys] for room in rooms]
    if any(not math.isfinite(x) or x < 0 for row in matrix for x in row):
        raise ValueError("Criterion values must be finite and nonnegative.")
    total = sum(weight_values)
    weights_normalized = [w / total for w in weight_values]
    norms = [math.hypot(*(row[j] for row in matrix)) for j in range(len(keys))]
    weighted = [
        [(x / norms[j] if norms[j] else 0.0) * weights_normalized[j]
         for j, x in enumerate(row)] for row in matrix
    ]
    positive, negative = [], []
    for j, key in enumerate(keys):
        column = [row[j] for row in weighted]
        low, high = min(column), max(column)
        benefit = CRITERIA[key][1]
        positive.append(high if benefit else low)
        negative.append(low if benefit else high)
    results = []
    for room, row in zip(rooms, weighted):
        d_plus = math.dist(row, positive)
        d_minus = math.dist(row, negative)
        denominator = d_plus + d_minus
        results.append({**room, "score": d_minus / denominator if denominator else 0.5,
                        "d_plus": d_plus, "d_minus": d_minus})
    return sorted(results, key=lambda room: (-room["score"], room["id"]))
