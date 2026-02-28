"""
Streamlit multi-page app entry point.
Run with: streamlit run frontend/app.py
"""
import streamlit as st
from frontend.pages import home, upload, query, history

st.set_page_config(
    page_title="Enterprise Doc Intelligence",
    page_icon="📄",
    layout="wide",
)

PAGES = {
    "🏠 Home": home,
    "📤 Upload Documents": upload,
    "🔍 Query": query,
    "📜 History": history,
}

with st.sidebar:
    st.title("📄 Doc Intelligence")
    selection = st.radio("Navigate", list(PAGES.keys()))

PAGES[selection].render()
