def enhance_prediction(prediction):

    plant_map = {
        "mango": "fruit tree",
        "banana": "fruit plant",
        "rose": "flowering plant"
    }

    health_status = "unknown"

    if "diseased" in prediction:
        health_status = "diseased"
    elif "healthy" in prediction:
        health_status = "healthy"

    return {
        "plant_type": plant_map.get(prediction, "unknown"),
        "health_status": health_status,
        "recommendation": "Keep plant healthy and monitor regularly."
    }