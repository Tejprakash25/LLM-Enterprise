"""API response models."""
from pydantic import BaseModel
from backend.models.schemas import DocumentMeta


class UploadResponse(BaseModel):
    message: str
    document: DocumentMeta


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[dict]
    latency_ms: float


class HealthResponse(BaseModel):
    status: str
    faiss_loaded: bool
    model: str
