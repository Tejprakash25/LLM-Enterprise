"""Prompt templates for the QA chain."""
from langchain.prompts import PromptTemplate

_TEMPLATE = """You are an expert enterprise document analyst.
Use ONLY the context below to answer the question. If the answer is not in the context, say "I don't have enough information to answer this."

Context:
{summaries}

Question: {question}

Answer (be concise and factual):"""

QA_CHAIN_PROMPT = PromptTemplate(
    input_variables=["summaries", "question"],
    template=_TEMPLATE,
)
