from fastapi import FastAPI
from routes.ocrRoute import router as ocr
app = FastAPI()

app.include_router(ocr)

@app.get("/")
def home():
    return {"message" : "Hello World"}

