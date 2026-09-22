def clip_to_study_area(feature_count: int, area_name: str = "Nagpur Demo Ward") -> dict:
    return {
        "mode": "demo",
        "area_name": area_name,
        "input_features": feature_count,
        "output_features": feature_count,
    }
