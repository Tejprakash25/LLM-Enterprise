"""Shared Pydantic schemas."""
from datetime import datetime
from pydantic import BaseModel


class DocumentMeta(BaseModel):
    doc_id: str
    filename: str
    file_type: str
    num_chunks: int
    uploaded_at: datetime
    ocr_applied: bool = False


class ChunkMeta(BaseModel):
    chunk_id: str
    doc_id: str
    page: int | None = None
    text_preview: str
