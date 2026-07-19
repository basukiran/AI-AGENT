from utils.chunker import chunk_text

text = """
Artificial Intelligence is amazing.
Machine Learning is a subset of AI.
Deep Learning uses Neural Networks.
"""

chunks = chunk_text(text, chunk_size=30)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}")
    print(chunk)
    print("-" * 30)