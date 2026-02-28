"""
CLI script: remove all uploads, processed docs, and FAISS index.
Usage: python scripts/clear_data.py
WARNING: This is destructive and irreversible.
"""
import shutil
from backend.core.config import settings
from loguru import logger


def clear_all():
    for path in [settings.UPLOAD_DIR, settings.PROCESSED_DIR, settings.FAISS_INDEX_PATH]:
        if path.exists():
            shutil.rmtree(path)
            path.mkdir(parents=True)
            logger.info(f"Cleared: {path}")


if __name__ == "__main__":
    confirm = input("This will delete ALL data. Type YES to confirm: ")
    if confirm.strip() == "YES":
        clear_all()
    else:
        print("Aborted.")
