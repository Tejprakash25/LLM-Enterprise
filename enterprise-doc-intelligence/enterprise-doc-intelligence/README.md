# Enterprise Document Intelligence System

LLM-powered RAG system for querying enterprise documents.

**Stack:** FastAPI · LangChain · FAISS · sentence-transformers (all-MiniLM-L6-v2) · Groq (Mixtral-8x7B) · Streamlit · Tesseract OCR

---

## Quick Start

### 1. Install dependencies (CPU-only, Windows-friendly)
```bash
pip install torch==2.3.1 --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

### 2. Configure environment
```bash
copy .env.example .env        # Windows
# Edit .env — add your GROQ_API_KEY
```

### 3. (Windows) Set Tesseract path in .env
```
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```

### 4. Ingest documents
```bash
python scripts/ingest_documents.py --folder data/uploads
```

### 5. Start the API
```bash
uvicorn backend.main:app --reload
```

### 6. Start the frontend
```bash
streamlit run frontend/app.py
```

---

## Project Structure
```
enterprise-doc-intelligence/
├── backend/          # FastAPI app
├── rag/              # LangChain chains, FAISS, embeddings
├── frontend/         # Streamlit UI
├── config/           # Shared settings
├── data/             # uploads, processed, faiss_index
├── scripts/          # CLI utilities
└── tests/            # unit + integration tests
```
