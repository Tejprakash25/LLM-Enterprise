"""
Multi-format document loader.
Supported: PDF, DOCX, PPTX, XLSX, TXT, images (via OCR).
"""
from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    UnstructuredPowerPointLoader,
    UnstructuredExcelLoader,
)
from backend.services.ocr.tesseract_engine import ocr_image_to_text
from backend.core.exceptions import UnsupportedFileTypeError

SUPPORTED_TYPES = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
    ".txt": TextLoader,
    ".md": TextLoader,
    ".pptx": UnstructuredPowerPointLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".xls": UnstructuredExcelLoader,
}
IMAGE_TYPES = {".png", ".jpg", ".jpeg", ".tiff", ".bmp"}


def load_document(file_path: str | Path):
    path = Path(file_path)
    suffix = path.suffix.lower()
    if suffix in SUPPORTED_TYPES:
        loader_cls = SUPPORTED_TYPES[suffix]
        return loader_cls(str(path)).load()
    if suffix in IMAGE_TYPES:
        text = ocr_image_to_text(path)
        from langchain.schema import Document
        return [Document(page_content=text, metadata={"source": str(path)})]
    raise UnsupportedFileTypeError(f"Unsupported file type: {suffix}")
