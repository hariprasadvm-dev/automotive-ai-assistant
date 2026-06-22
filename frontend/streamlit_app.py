import sys
import os
import streamlit as st

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app.rag_engine import ask_question

st.set_page_config(
    page_title="Automotive AI Assistant",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Automotive AI Assistant")
st.caption("Ask questions from AUTOSAR, ISO 26262, CAN, ECU, and diagnostics documents.")

with st.sidebar:
    st.header("Project Info")
    st.write("RAG-based assistant using ChromaDB, LangChain, Ollama, and local documents.")
    st.markdown("---")
    st.write("Example questions:")
    st.code("What is CAN arbitration?")
    st.code("Explain ASIL levels.")
    st.code("What is UDS diagnostics?")
    st.code("Explain AUTOSAR communication stack.")

    if st.button("Clear chat"):
        st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Ask an automotive engineering question...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents and generating answer..."):
            response = ask_question(query, st.session_state.messages)
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )