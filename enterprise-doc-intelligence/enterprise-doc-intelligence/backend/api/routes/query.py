"""Query / Q&A endpoint."""
import time
from fastapi import APIRouter, HTTPException
from backend.models.requests import QueryRequest
from backend.models.responses import QueryResponse

router = APIRouter()


@router.post("/", response_model=QueryResponse)
async def query_documents(request: QueryRequest):
    # TODO: load FAISS store, build chain, run query
    start = time.time()
    raise HTTPException(status_code=501, detail="Not implemented yet")
