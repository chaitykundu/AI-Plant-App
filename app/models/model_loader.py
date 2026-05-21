import torch
import torchvision.models as models


def load_model():

    model = models.efficientnet_b0(pretrained=True)

    model.eval()

    return model