from pydantic import BaseModel
from typing import List
from datetime import datetime


class PlantInfo(BaseModel):
    common_name: str
    scientific_name: str
    family: str


class PlantResponse(BaseModel):
    success: bool
    plant: PlantInfo
    confidence: float
    care_tips: List[str]
    detected_at: datetime