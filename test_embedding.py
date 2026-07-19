from utils.chunker import chunk_text
from utils.embeddings import generate_embedding

text = """
Artificial Intelligence is amazing.
Machine Learning is a subset of AI.
Deep Learning uses Neural Networks.
"""

chunks = chunk_text(text)

all_embeddings = []

for chunk in chunks:
    vector = generate_embedding(chunk)
    all_embeddings.append(vector)

print("Total Chunks:", len(chunks))
print("Total Embeddings:", len(all_embeddings))