import torch

from app.models.model_loader import load_model
from app.services.image_preprocessing import preprocess_image
from app.core.constants import PLANT_CLASSES

model = load_model()


def predict_plant(image_path):

    print("\n========== 🌿 PLANT PREDICTION DEBUG ==========")
    print(f"[DEBUG] Image Path: {image_path}")

    image_tensor = preprocess_image(image_path)
    print(f"[DEBUG] Input Tensor Shape: {image_tensor.shape}")

    with torch.no_grad():
        outputs = model(image_tensor)

    print(f"[DEBUG] Raw Model Output: {outputs}")

    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

    print(f"[DEBUG] Probabilities: {probabilities}")

    confidence, predicted_class = torch.max(probabilities, 0)

    confidence = round(confidence.item() * 100, 2)
    predicted_class = predicted_class.item()

    print(f"[DEBUG] Predicted Class Index: {predicted_class}")
    print(f"[DEBUG] Confidence: {confidence}%")

    print(f"[DEBUG] PLANT_CLASSES keys: {list(PLANT_CLASSES.keys())}")

    plant_data = PLANT_CLASSES.get(predicted_class)

    if plant_data is None:
        print("[DEBUG] ❌ Class not found in PLANT_CLASSES")
        print("========== END DEBUG ==========\n")

        return {
            "success": False,
            "message": "Plant not found",
            "predicted_class": predicted_class,
            "confidence": confidence
        }

    print(f"[DEBUG] ✅ Plant Found: {plant_data}")
    print("========== END DEBUG ==========\n")

    return {
        "success": True,
        "plant": plant_data,
        "confidence": confidence
    }