"""HTTP client for communicating with the FastAPI backend."""
import requests
from backend.core.config import settings

BASE_URL = settings.STREAMLIT_API_URL


def upload_document(file_bytes: bytes, filename: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/api/documents/upload",
        files={"file": (filename, file_bytes)},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()


def query_documents(question: str, top_k: int = 4) -> dict:
    resp = requests.post(
        f"{BASE_URL}/api/query/",
        json={"question": question, "top_k": top_k},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


def list_documents() -> list[dict]:
    resp = requests.get(f"{BASE_URL}/api/documents/list", timeout=10)
    resp.raise_for_status()
    return resp.json().get("documents", [])
