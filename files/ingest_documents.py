"""
CLI script: bulk-ingest a folder of documents into the FAISS index.
Usage: python scripts/ingest_documents.py --folder data/uploads
"""
import argparse
from pathlib import Path
from loguru import logger
from backend.services.ingestion.document_loader import load_document
from backend.services.ingestion.text_splitter import split_documents
from rag.vectorstore.faiss_store import load_or_create_store, save_store
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.core.config import settings


def ingest_folder(folder: Path) -> None:
    files = list(folder.iterdir())
    logger.info(f"Found {len(files)} files in {folder}")
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
        model_kwargs={"device": settings.EMBEDDING_DEVICE},
    )
    store = load_or_create_store()

    for fp in files:
        if fp.name.startswith("."):
            continue
        try:
            docs = load_document(fp)
            chunks = split_documents(docs)
            if store is None:
                store = FAISS.from_documents(chunks, embeddings)
            else:
                store.add_documents(chunks)
            logger.info(f"Ingested {fp.name} → {len(chunks)} chunks")
        except Exception as exc:
            logger.error(f"Failed to ingest {fp.name}: {exc}")

    if store:
        save_store(store)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=Path, default=Path("data/uploads"))
    args = parser.parse_args()
    ingest_folder(args.folder)
