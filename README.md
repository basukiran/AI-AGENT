# 🤖 AI PDF Assistant

A Local AI-powered PDF Question Answering application built using **Python, Streamlit, Ollama, Qwen2.5, FAISS, and PyMuPDF**.

Users can upload a PDF and ask questions in natural language. The application retrieves relevant information using **Retrieval-Augmented Generation (RAG)** and generates accurate responses using a local LLM.

## 🚀 Features

- 📄 Upload PDF documents
- 📖 Extract text from PDFs
- ✂️ Automatic text chunking
- 🧠 Generate embeddings
- 🔍 Semantic search using FAISS
- 🤖 AI-powered question answering
- 💬 Interactive Streamlit interface
- 🔒 Runs completely offline

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama
- Qwen2.5
- nomic-embed-text
- FAISS
- PyMuPDF

## 📂 Project Structure

```
AI_Assistant_LLM/
│── app.py
│── utils/
│── data/
│── requirements.txt
└── README.md
```

## ▶️ Installation

```bash
git clone https://github.com/basukiran/AI-AGENT.git
cd AI_PDF_Assistant

pip install -r requirements.txt

ollama pull qwen2.5:3b
ollama pull nomic-embed-text

ollama serve

streamlit run app.py
```

## 📌 Future Improvements

- Multiple PDF support
- Conversation memory
- Source citations
- Modern UI
- Cloud deployment

## 👨‍💻 Author

**Basukiran Dadibavi**

Artificial Intelligence & Machine Learning Student
