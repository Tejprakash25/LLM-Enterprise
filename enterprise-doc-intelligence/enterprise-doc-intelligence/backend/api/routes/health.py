"""Health check endpoint."""
from fastapi import APIRouter
from backend.models.responses import HealthResponse
from backend.core.config import settings

router = APIRouter()


@router.get("/", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="ok",
        faiss_loaded=True,   # TODO: wire up actual store state
        model=settings.GROQ_MODEL_NAME,
    )
