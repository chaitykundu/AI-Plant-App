import os
import aiofiles

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_upload_file(file):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    return file_path