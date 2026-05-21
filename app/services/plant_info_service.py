PLANT_CARE_DATA = {
    "Banana": {
        "care_tips": [
            "Needs warm temperature",
            "Water regularly",
            "Requires full sunlight"
        ]
    },

    "Mango": {
        "care_tips": [
            "Needs deep watering",
            "Grow in sunny place",
            "Avoid overwatering"
        ]
    }
}


def get_plant_care(common_name: str):
    return PLANT_CARE_DATA.get(
        common_name,
        {"care_tips": ["No care tips available"]}
    )