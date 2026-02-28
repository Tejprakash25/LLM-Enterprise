"""
CLI script: wipe and rebuild the FAISS index from all processed documents.
Usage: python scripts/rebuild_index.py
"""
import shutil
from pathlib import Path
from backend.core.config import settings
from loguru import logger
from scripts.ingest_documents import ingest_folder


def rebuild():
    idx_path = settings.FAISS_INDEX_PATH
    if idx_path.exists():
        shutil.rmtree(idx_path)
        logger.info(f"Cleared index at {idx_path}")
    idx_path.mkdir(parents=True, exist_ok=True)
    ingest_folder(settings.PROCESSED_DIR)


if __name__ == "__main__":
    rebuild()
