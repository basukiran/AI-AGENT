import faiss
import numpy as np

# Five sample vectors (dimension = 4)
vectors = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
    [0.9, 0.1, 0.0, 0.0]
], dtype="float32")

dimension = 4

index = faiss.IndexFlatL2(dimension)

index.add(vectors)

print("Vectors stored:", index.ntotal)