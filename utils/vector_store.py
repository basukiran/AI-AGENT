import faiss
import numpy as np

class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add(self, embeddings, texts):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_embedding, k=3):

        query = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query, k)

        results = []

        for idx in indices[0]:
            if idx != -1:
                results.append(self.texts[idx])

        return results