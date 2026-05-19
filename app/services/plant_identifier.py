from transformers import pipeline
from PIL import Image

classifier = pipeline(
    "zero-shot-image-classification",
    model="openai/clip-vit-base-patch32"
)

PLANT_LABELS = [
    "rose plant",
    "sunflower plant",
    "mango tree",
    "banana plant",
    "tomato plant"
]

HEALTH_LABELS = [
    "healthy leaf",
    "diseased leaf"
]

def get_top_result(results):
    return max(results, key=lambda x: x["score"])


def identify_plant(image_path):
    image = Image.open(image_path)

    # Step 1: plant type
    plant_results = classifier(image, candidate_labels=PLANT_LABELS)
    plant_top = get_top_result(plant_results)

    # Step 2: health
    health_results = classifier(image, candidate_labels=HEALTH_LABELS)
    health_top = get_top_result(health_results)

    plant_name = plant_top["label"]
    plant_conf = round(plant_top["score"] * 100, 2)

    health_label = health_top["label"]
    health_conf = round(health_top["score"] * 100, 2)

    health_status = "Healthy" if "healthy" in health_label else "Diseased"

    return {
        "success": True,
        "plant_name": plant_name,
        "scientific_name": plant_name,
        "confidence": plant_conf,
        "health_status": health_status,
        "health_confidence": health_conf,
        "message": "Plant identified successfully"
    }