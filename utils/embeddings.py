from ollama import embed

MODEL_NAME = "nomic-embed-text"


def generate_embedding(text):
    response = embed(
        model=MODEL_NAME,
        input=text
    )

    return response["embeddings"][0]