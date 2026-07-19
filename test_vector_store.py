from utils.vector_store import VectorStore
from utils.embeddings import generate_embedding

texts = [
    "Python is a programming language.",
    "TensorFlow is used for Deep Learning.",
    "Football is a popular sport."
]

embeddings = [generate_embedding(text) for text in texts]

dimension = len(embeddings[0])

store = VectorStore(dimension)
store.add_embeddings(embeddings)

query = "Which framework is used for deep learning?"

query_embedding = generate_embedding(query)

distances, indices = store.search(query_embedding)

print("Distances:", distances)
print("Indices:", indices)

print("Best Match:", texts[indices[0][0]])