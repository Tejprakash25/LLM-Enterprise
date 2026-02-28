"""
FAISS local persistent vector store.
Index is saved/loaded from disk so it survives restarts.
"""
import pickle
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.core.config import settings
from loguru import logger


def _get_hf_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
        model_kwargs={"device": settings.EMBEDDING_DEVICE},
    )


def load_or_create_store() -> FAISS:
    index_path = settings.FAISS_INDEX_PATH / settings.FAISS_INDEX_NAME
    embeddings = _get_hf_embeddings()
    if index_path.with_suffix(".faiss").exists():
        logger.info(f"Loading FAISS index from {index_path}")
        return FAISS.load_local(
            str(settings.FAISS_INDEX_PATH),
            embeddings,
            index_name=settings.FAISS_INDEX_NAME,
            allow_dangerous_deserialization=True,
        )
    logger.info("No existing FAISS index found — will create on first ingest.")
    return None


def save_store(store: FAISS) -> None:
    settings.FAISS_INDEX_PATH.mkdir(parents=True, exist_ok=True)
    store.save_local(
        str(settings.FAISS_INDEX_PATH),
        index_name=settings.FAISS_INDEX_NAME,
    )
    logger.info("FAISS index saved.")
