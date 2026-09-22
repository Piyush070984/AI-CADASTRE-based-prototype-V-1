from collections.abc import Iterable


def validate_geometry_records(records: Iterable[dict]) -> dict:
    total = 0
    invalid = 0
    for record in records:
        total += 1
        if "geometry" not in record:
            invalid += 1
    return {"mode": "demo", "total": total, "invalid": invalid}
