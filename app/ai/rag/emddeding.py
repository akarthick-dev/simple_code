
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)


def em_model(chunks: list[str]) -> list[list[float]]:
    if not chunks:
        return []

    prefixed = [f"search_document: {chunk}" for chunk in chunks]
    embeddings = model.encode(prefixed)
    return embeddings.tolist()
