from pydantic import BaseModel

class PlantResponse(BaseModel):
    plant_name: str
    scientific_name: str
    confidence: float