"""Recursive character text splitter configured from settings."""
from langchain.text_splitter import RecursiveCharacterTextSplitter
from backend.core.config import settings


def get_splitter() -> RecursiveCharacterTextSplitter:
    return RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )


def split_documents(documents):
    splitter = get_splitter()
    return splitter.split_documents(documents)
