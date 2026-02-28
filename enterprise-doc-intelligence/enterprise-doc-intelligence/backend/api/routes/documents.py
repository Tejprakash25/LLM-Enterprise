"""Document ingestion endpoints."""
from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.models.responses import UploadResponse

router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    # TODO: validate, save, ingest pipeline
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/list")
async def list_documents():
    # TODO: return indexed document metadata
    return {"documents": []}


@router.delete("/{doc_id}")
async def delete_document(doc_id: str):
    # TODO: remove from FAISS + disk
    raise HTTPException(status_code=501, detail="Not implemented yet")
