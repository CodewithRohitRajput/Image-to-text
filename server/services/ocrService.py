import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def image_to_text(file):
    image = Image.open(io.BytesIO(file.file.read()))
    text = pytesseract.image_to_string(image)
    return text