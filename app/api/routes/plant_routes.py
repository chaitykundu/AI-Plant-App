from fastapi import APIRouter, UploadFile, File
from app.utils.file_handler import save_upload_file
from app.services.plant_identifier import identify_plant

router = APIRouter(
    prefix="/plant",
    tags=["Plant AI"]
)

@router.post("/identify")
async def identify(file: UploadFile = File(...)):

    file_path = await save_upload_file(file)

    result = identify_plant(file_path)

    return result