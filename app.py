import os
import streamlit as st

from utils.pdf_reader import read_pdf
from utils.chunker import chunk_text
from utils.embeddings import generate_embedding
from utils.vector_store import VectorStore
from utils.rag import ask_rag

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI PDF Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI PDF Assistant")
st.write("Upload a PDF and ask questions about it.")

# --------------------------------------------------
# Create folders
# --------------------------------------------------

os.makedirs("data", exist_ok=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:
    st.header("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        file_path = os.path.join(
            "data",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("PDF Uploaded")

        # ------------------------
        # Read PDF
        # ------------------------

        with st.spinner("Reading PDF..."):
            text = read_pdf(file_path)

        # ------------------------
        # Chunking
        # ------------------------

        with st.spinner("Creating Chunks..."):
            chunks = chunk_text(
                text,
                chunk_size=500
            )

        st.write(f"Chunks : {len(chunks)}")

        # ------------------------
        # Embeddings
        # ------------------------

        embeddings = []

        progress = st.progress(0)

        for i, chunk in enumerate(chunks):

            embedding = generate_embedding(chunk)

            embeddings.append(embedding)

            progress.progress(
                (i + 1) / len(chunks)
            )

        # ------------------------
        # Vector Store
        # ------------------------

        dimension = len(embeddings[0])

        vector_store = VectorStore(dimension)

        vector_store.add(
            embeddings,
            chunks
        )

        st.session_state.vector_store = vector_store

        st.success("✅ PDF Indexed Successfully")

# --------------------------------------------------
# Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# User Question
# --------------------------------------------------

question = st.chat_input(
    "Ask anything from the uploaded PDF..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        if st.session_state.vector_store is None:

            answer = "⚠️ Please upload a PDF first."

            st.error(answer)

        else:

            with st.spinner("Searching..."):

                try:

                    answer = ask_rag(
                        question,
                        st.session_state.vector_store
                    )

                    st.markdown(answer)

                except Exception as e:

                    answer = f"Error: {e}"

                    st.error(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )