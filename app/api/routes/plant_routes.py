from fastapi import APIRouter, UploadFile, File
from datetime import datetime

from app.services.plant_identifier import predict_plant
from app.services.plant_info_service import get_plant_care
from app.services.disease_detector import detect_disease
from app.utils.file_handler import save_upload_file

router = APIRouter()


@router.post("/identify")
async def identify_plant(file: UploadFile = File(...)):

    file_location = await save_upload_file(file)

    prediction = predict_plant(file_location)

    if prediction["success"] is False:
        return prediction

    disease_data = detect_disease(file_location)

    plant = prediction["plant"]

    care_data = get_plant_care(
        plant["common_name"]
    )

    return {
        "success": True,
        "plant": plant,
        "confidence": prediction["confidence"],
        "care_tips": care_data["care_tips"],

        "disease": disease_data,

        "detected_at": datetime.now()
    }