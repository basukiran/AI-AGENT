from utils.chunker import chunk_text
from utils.embeddings import generate_embedding
from utils.vector_store import VectorStore
from utils.rag import ask_rag

text = """
Python is a programming language.

TensorFlow is used for Deep Learning.

Machine Learning is a subset of Artificial Intelligence.
"""

chunks = chunk_text(text, chunk_size=100)

embeddings = [generate_embedding(chunk) for chunk in chunks]

store = VectorStore(len(embeddings[0]))
store.add(embeddings, chunks)

question = "Which framework is used for deep learning?"

answer = ask_rag(question, store)
print(answer)