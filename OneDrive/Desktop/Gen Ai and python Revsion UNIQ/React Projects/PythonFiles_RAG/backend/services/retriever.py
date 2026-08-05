"""
services/retriever.py

Hybrid RAG Retriever

Responsibilities
----------------
1. Convert Recruiter Query into Embedding
2. Perform Vector Similarity Search
3. Apply Metadata Filters
4. Retrieve Top-K Resume Chunks
5. Send Results to Reranker
"""

from sentence_transformers import SentenceTransformer

from PythonFiles_RAG.backend.utils.config import settings
from PythonFiles_RAG.backend.utils.logger import logger

from PythonFiles_RAG.backend.services.vector_service import similarity_search


# ==========================================================
# Load Embedding Model
# ==========================================================

embedding_model = SentenceTransformer(
    settings.EMBEDDING_MODEL
)


# ==========================================================
# Query Embedding
# ==========================================================

def generate_query_embedding(query: str):

    """
    Convert recruiter query into embedding.
    """

    embedding = embedding_model.encode(

        query,

        normalize_embeddings=True

    )

    return embedding.tolist()


# ==========================================================
# Hybrid Retrieval
# ==========================================================

def retrieve_documents(

    query: str,

    top_k: int = 5,

    metadata_filter: dict = None

):

    """
    Retrieve relevant resume chunks.
    """

    logger.info("Retrieval Started")

    # --------------------------------------
    # Query Embedding
    # --------------------------------------

    query_embedding = generate_query_embedding(query)

    # --------------------------------------
    # Pinecone Search
    # --------------------------------------

    matches = similarity_search(

        query_embedding=query_embedding,

        top_k=top_k,

        filters=metadata_filter

    )

    documents = []

    for match in matches:

        documents.append({

            "id": match.id,

            "score": match.score,

            "resume_id": match.metadata.get("resume_id"),

            "section": match.metadata.get("section"),

            "text": match.metadata.get("text")

        })

    logger.info(

        f"{len(documents)} Resume Chunks Retrieved"

    )

    return documents


# ==========================================================
# Retrieve by Skills
# ==========================================================

def retrieve_by_skills(

    query: str,

    skills: list,

    top_k: int = 5

):

    metadata_filter = {

        "skills": {

            "$in": skills

        }

    }

    return retrieve_documents(

        query=query,

        top_k=top_k,

        metadata_filter=metadata_filter

    )


# ==========================================================
# Retrieve by Experience
# ==========================================================

def retrieve_by_experience(

    query: str,

    experience: float,

    top_k: int = 5

):

    metadata_filter = {

        "experience": {

            "$gte": experience

        }

    }

    return retrieve_documents(

        query=query,

        top_k=top_k,

        metadata_filter=metadata_filter

    )


# ==========================================================
# Retrieve by Location
# ==========================================================

def retrieve_by_location(

    query: str,

    location: str,

    top_k: int = 5

):

    metadata_filter = {

        "location": {

            "$eq": location

        }

    }

    return retrieve_documents(

        query=query,

        top_k=top_k,

        metadata_filter=metadata_filter

    )