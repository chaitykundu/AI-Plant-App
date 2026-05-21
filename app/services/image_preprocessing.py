from PIL import Image
import torchvision.transforms as transforms


def preprocess_image(image_path):

    image = Image.open(image_path).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    image_tensor = transform(image)

    return image_tensor.unsqueeze(0)