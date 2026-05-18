from transformers import pipeline
from PIL import Image

# Load CLIP model (zero-shot)
classifier = pipeline(
    "zero-shot-image-classification",
    model="openai/clip-vit-base-patch32"
)

def identify_plant(image_path):

    image = Image.open(image_path)

    # Plant-specific labels (you control this)
    labels = [
        "rose plant",
        "sunflower plant",
        "mango tree",
        "banana plant",
        "tomato plant",
        "healthy leaf",
        "diseased leaf",
        "unknown plant"
    ]

    results = classifier(image, candidate_labels=labels)

    top_result = results[0]

    return {
        "prediction": top_result["label"],
        "confidence": round(top_result["score"] * 100, 2)
    } 