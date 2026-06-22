# 🚗 Automotive AI Assistant

An AI-powered Retrieval-Augmented Generation (RAG) assistant for automotive engineering documentation.

The assistant allows engineers to query AUTOSAR specifications, ISO 26262 safety documents, CAN protocol documentation, ECU specifications, diagnostics manuals, and other technical documents using natural language.

Built using local LLMs, vector databases, semantic search, and Streamlit.

---

## Features

### Document Intelligence
- PDF document ingestion
- Semantic search using embeddings
- Context-aware question answering
- Local document retrieval

### Automotive Knowledge Support
- AUTOSAR architecture
- ISO 26262 functional safety
- CAN communication
- UDS diagnostics
- ECU specifications
- Automotive software documentation

### AI Components
- Retrieval-Augmented Generation (RAG)
- Local LLM inference via Ollama
- Vector database storage
- Embedding-based document retrieval

### User Interface
- ChatGPT-style Streamlit UI
- Chat history
- Real-time responses
- Local execution

---

## Architecture

```text
                    User Question
                           │
                           ▼
                    Streamlit UI
                           │
                           ▼
                      Retriever
                      (ChromaDB)
                           │
                           ▼
                 Relevant Documents
                           │
                           ▼
                    Prompt Builder
                           │
                           ▼
                     Ollama LLM
                      (Llama 3)
                           │
                           ▼
                      Response
```

---

## Tech Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Ollama |
| Model | Llama 3 |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| RAG Framework | LangChain |
| PDF Processing | PyPDF |
| Environment | Python 3.11 |

---

## Project Structure

```text
automotive-rag-assistant/
│
├── app/
│   ├── __init__.py
│   ├── ingest.py
│   ├── rag_engine.py
│
├── frontend/
│   └── streamlit_app.py
│
├── documents/
│
├── chroma_db/
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/automotive-ai-assistant.git

cd automotive-ai-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the model:

```bash
ollama pull llama3
```

Verify:

```bash
ollama run llama3
```

---

## Add Documents

Place PDF files inside:

```text
documents/
```

Examples:

- AUTOSAR specifications
- ISO 26262 documents
- CAN protocol documentation
- ECU manuals
- Diagnostics manuals

---

## Create Vector Database

Run document ingestion:

```bash
python app/ingest.py
```

This will:

1. Load PDFs
2. Split documents into chunks
3. Generate embeddings
4. Store vectors in ChromaDB

---

## Run Application

Start Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

---

## Example Questions

```text
What is CAN arbitration?

Explain AUTOSAR communication stack.

What is ASIL-D?

Explain UDS diagnostics.

What causes CAN bus overload?

Summarize ISO 26262 safety lifecycle.
```




