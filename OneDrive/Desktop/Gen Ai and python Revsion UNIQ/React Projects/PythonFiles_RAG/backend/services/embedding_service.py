"""
services/embedding_service.py

Embedding Generation Service

Responsibilities
----------------
1. Load Embedding Model
2. Generate Embeddings
3. Store Embeddings in Pinecone
"""

from sentence_transformers import SentenceTransformer
from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.utils.config import settings
from PythonFiles_RAG.backend.utils.logger import logger

from PythonFiles_RAG.backend.services.vector_service import store_embeddings


# ==========================================================
# Load Embedding Model
# ==========================================================

embedding_model = SentenceTransformer(
    settings.EMBEDDING_MODEL
)


# ==========================================================
# Generate Embedding
# ==========================================================

def generate_embedding(text: str):

    """
    Generate embedding vector for a text chunk.
    """

    vector = embedding_model.encode(
        text,
        normalize_embeddings=True
    )

    return vector.tolist()


# ==========================================================
# Generate Embeddings
# ==========================================================

def generate_embeddings(

    resume_id: int,

    chunks: list,

    db: Session

):

    """
    Generate embeddings for semantic chunks.
    """

    logger.info("Embedding Generation Started")

    vectors = []

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(

            chunk["text"]

        )

        vectors.append({

            "id": f"{resume_id}_{index+1}",

            "values": embedding,

            "metadata": {

                "resume_id": resume_id,

                "section": chunk["section"],

                "text": chunk["text"]

            }

        })

    # ---------------------------------------------
    # Store in Pinecone
    # ---------------------------------------------

    store_embeddings(vectors)

    logger.info(

        f"{len(vectors)} Embeddings Generated"

    )

    return vectors