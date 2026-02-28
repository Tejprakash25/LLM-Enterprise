"""
Sentence-Transformers embedder wrapper.
Model: all-MiniLM-L6-v2  |  Device: CPU
"""
from functools import lru_cache
from sentence_transformers import SentenceTransformer
from backend.core.config import settings
from loguru import logger


@lru_cache(maxsize=1)
def get_embedder() -> SentenceTransformer:
    logger.info(f"Loading embedding model: {settings.EMBEDDING_MODEL}")
    return SentenceTransformer(
        settings.EMBEDDING_MODEL,
        device=settings.EMBEDDING_DEVICE,
    )


def embed_texts(texts: list[str]) -> list[list[float]]:
    model = get_embedder()
    return model.encode(texts, show_progress_bar=False).tolist()
