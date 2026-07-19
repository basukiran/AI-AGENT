from ollama import chat
from utils.embeddings import generate_embedding


def ask_rag(question, vector_store):
    # Generate embedding for the user's question
    query_embedding = generate_embedding(question)

    # Search FAISS
    relevant_chunks = vector_store.search(query_embedding, k=3)

    # Combine retrieved chunks
    context = "\n\n".join(relevant_chunks)

    # Build the prompt
    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context, reply:
"I couldn't find the answer in the uploaded document."
"""

    # Ask Qwen
    response = chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]