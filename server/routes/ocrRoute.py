from fastapi import APIRouter, UploadFile, File
from services.ocrService import image_to_text

router = APIRouter(prefix="/text", tags=["OCR"])

@router.post("/")
async def extract_text(file : UploadFile = File(...)):
    text = image_to_text(file)
    return {"text" : text}

