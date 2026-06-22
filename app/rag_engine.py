from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM

DB_PATH = "chroma_db"

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)

# Retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

# Local LLM
llm = OllamaLLM(model="llama3")


def ask_question(query, chat_history=None):

    if chat_history is None:
        chat_history = []

    history_text = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in chat_history[-6:]
        ]
    )

    enhanced_query = f"""
Chat history:
{history_text}

Current question:
{query}
"""

    docs = retriever.invoke(enhanced_query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an automotive engineering AI assistant.

Use the provided document context and chat history to answer.
If the user asks a follow-up question, understand it from the previous conversation.

Chat history:
{history_text}

Document context:
{context}

Current question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response