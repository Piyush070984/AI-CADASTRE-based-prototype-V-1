def export_geojson(features: list[dict]) -> dict:
    return {
        "type": "FeatureCollection",
        "metadata": {
            "mode": "demo",
            "warning": "Demo export from scaffolded GIS module.",
        },
        "features": features,
    }


def export_csv_rows(rows: list[dict]) -> list[dict]:
    return rows
