"""
Retrieval-Augmented QA chain using Groq (Mixtral-8x7B) + FAISS.
"""
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from rag.prompts.qa_prompts import QA_CHAIN_PROMPT
from backend.core.config import settings


def build_qa_chain(store: FAISS, top_k: int = 4):
    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model_name=settings.GROQ_MODEL_NAME,
        temperature=0.1,
    )
    retriever = store.as_retriever(search_kwargs={"k": top_k})
    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        return_source_documents=True,
    )
    return chain
