# Image to Text API

Simple FastAPI service that wraps Tesseract OCR to convert uploaded images into plain text. The service exposes a single `/text/` endpoint that accepts an image file upload and returns extracted text.

## Project Layout
- `server/server.py` – FastAPI app setup and router registration
- `server/routes/ocrRoute.py` – `/text/` route definition
- `server/services/ocrService.py` – OCR logic using Tesseract
- `client/` – placeholder for a future frontend (currently empty)

## Requirements
- Python 3.9+ (tested on Windows)
- Tesseract OCR installed locally
  - Default path in code: `C:\Program Files\Tesseract-OCR\tesseract.exe`
  - If Tesseract is installed elsewhere, update `pytesseract.pytesseract.tesseract_cmd` in `server/services/ocrService.py`

## Setup
1) Clone and enter the project
```bash
git clone <your-fork-url>
cd Image_to_Text
```
2) (Recommended) create and activate a virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate
```
3) Install Python dependencies
```bash
pip install fastapi uvicorn pillow pytesseract python-multipart
```
4) Ensure Tesseract is installed and on your system
- Download for Windows: https://github.com/UB-Mannheim/tesseract/wiki
- Confirm the path matches the value set in `server/services/ocrService.py`

## Run the API
From the repo root:
```bash
uvicorn server.server:app --reload --port 8000
```
The API will be available at `http://localhost:8000` and auto-reloads on code changes.

## Usage
Send a `POST` with `multipart/form-data` containing an image file to `/text/`.

Example with `curl`:
```bash
curl -X POST "http://localhost:8000/text/" \
  -F "file=@/path/to/image.png" \
  -H "Accept: application/json"
```
Response example:
```json
{
  "text": "Recognized text from the image"
}
```

## Notes
- Supported formats depend on Pillow (common: PNG, JPG, BMP, TIFF).
- OCR quality improves with high-contrast, high-resolution images.
- If you hit a `TesseractNotFoundError`, re-check the installed path and the `tesseract_cmd` setting.
