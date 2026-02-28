"""
Tesseract OCR engine wrapper.
Windows path to tesseract.exe is read from settings (TESSERACT_CMD env var).
"""
from pathlib import Path
import pytesseract
from PIL import Image
from backend.core.config import settings
from backend.core.exceptions import OCRError

pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD


def ocr_image_to_text(image_path: str | Path) -> str:
    try:
        img = Image.open(image_path)
        return pytesseract.image_to_string(img, lang=settings.OCR_LANGUAGE)
    except Exception as exc:
        raise OCRError(f"OCR failed for {image_path}: {exc}") from exc
