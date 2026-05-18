from dotenv import load_dotenv
import os

load_dotenv()

PLANT_ID_API_KEY = os.getenv("PLANT_ID_API_KEY")
print("PLANT_ID_API_KEY:", PLANT_ID_API_KEY)