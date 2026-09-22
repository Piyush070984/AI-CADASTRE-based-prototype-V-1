def read_crs_metadata(source_name: str) -> dict:
    return {
        "mode": "demo",
        "source": source_name,
        "crs": "EPSG:4326",
        "note": "Replace with actual dataset CRS detection in production GIS pipeline.",
    }
