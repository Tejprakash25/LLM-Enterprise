"""API request models."""
from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=1000)
    top_k: int = Field(default=4, ge=1, le=20)
    doc_filter: list[str] | None = None   # optional list of doc_ids to scope search
