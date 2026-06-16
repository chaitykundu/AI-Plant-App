# AI-Plant-App
🌿 Plant App – Plant Species Classification

This is a simple AI-based web API that can identify plant species from images. It uses a deep learning model built with PyTorch and is served through FastAPI.

The idea behind this project was to practice deploying a real ML model in a clean backend setup and make it usable through an API.

What this project does
-Takes an image of a plant as input
-Processes the image and runs it through a trained model
-Returns the predicted plant name with confidence score

Tech stack
- Python
- FastAPI
- PyTorch
- Torchvision
- Uvicorn
- PIL (Pillow)

Project structure:
AI-Plant-App/
│
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── models/             # Model loading code
│   ├── services/           # Image processing + prediction logic
│   └── core/               # Constants and config
│
├── models/
│   └── plant_model.pth     # Trained model weights
│
├── requirements.txt
└── README.md

How to run it locally
1. Clone the project

git clone https://github.com/your-username/AI-Plant-App.git
cd AI-Plant-App

2. Create a virtual environment

python -m venv venv

3. Activate it

On Windows:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Start the server

uvicorn app.main:app --reload