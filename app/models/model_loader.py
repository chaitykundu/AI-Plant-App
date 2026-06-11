import torch
import torchvision.models as models
import torch.nn as nn

from app.core.constants import PLANT_CLASSES


def load_model():

    # 1. Load base model
    model = models.efficientnet_b0(pretrained=True)

    # 2. Get number of your plant classes
    num_classes = len(PLANT_CLASSES)

    # 3. Replace classifier (IMPORTANT FIX)
    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        num_classes
    )

    # 4. Load trained weights (if available)
    # ⚠️ If you don't have trained model yet, keep this commented
    # model.load_state_dict(torch.load("plant_model.pth", map_location="cpu"))

    model.eval()

    return model