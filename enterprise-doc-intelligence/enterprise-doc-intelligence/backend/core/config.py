"""
Centralised settings loaded from .env via pydantic-settings.
All paths use forward slashes — pathlib handles OS conversion at runtime.
"""
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # LLM
    GROQ_API_KEY: str = ""
    GROQ_MODEL_NAME: str = "mixtral-8x7b-32768"

    # Embeddings
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    EMBEDDING_DEVICE: str = "cpu"

    # Vector store
    FAISS_INDEX_PATH: Path = Path("data/faiss_index")
    FAISS_INDEX_NAME: str = "doc_index"

    # Document processing
    UPLOAD_DIR: Path = Path("data/uploads")
    PROCESSED_DIR: Path = Path("data/processed")
    MAX_FILE_SIZE_MB: int = 50
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 64

    # OCR
    TESSERACT_CMD: str = "tesseract"
    OCR_LANGUAGE: str = "eng"

    # API
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    API_RELOAD: bool = True
    LOG_LEVEL: str = "INFO"

    # Streamlit
    STREAMLIT_API_URL: str = "http://127.0.0.1:8000"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
