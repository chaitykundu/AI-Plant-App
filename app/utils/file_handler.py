import os
import aiofiles
import uuid

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_upload_file(file):
    # safer unique filename
    ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    file_path = os.path.join(UPLOAD_DIR, filename)

    content = await file.read()

    async with aiofiles.open(file_path, "wb") as out_file:
        await out_file.write(content)

    return file_path