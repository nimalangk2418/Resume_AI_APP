"""
services/vector_service.py

Vector Database Service

Responsibilities
----------------
1. Connect to Pinecone
2. Create/Connect Index
3. Store Embeddings
4. Perform Similarity Search
5. Delete Embeddings
"""

from pinecone import Pinecone, ServerlessSpec

from PythonFiles_RAG.backend.utils.config import settings
from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Initialize Pinecone
# ==========================================================

pc = Pinecone(
    api_key=settings.PINECONE_API_KEY
)


# ==========================================================
# Create Index (if not exists)
# ==========================================================

index_name = settings.PINECONE_INDEX

existing_indexes = [

    index["name"]

    for index in pc.list_indexes()

]

if index_name not in existing_indexes:

    pc.create_index(

        name=index_name,

        dimension=384,

        metric="cosine",

        spec=ServerlessSpec(

            cloud="aws",

            region="us-east-1"

        )

    )

    logger.info(f"Pinecone Index Created : {index_name}")


# ==========================================================
# Connect Index
# ==========================================================

index = pc.Index(index_name)


# ==========================================================
# Store Embeddings
# ==========================================================

def store_embeddings(vectors):

    """
    Store vectors inside Pinecone.
    """

    try:

        index.upsert(

            vectors=vectors

        )

        logger.info(

            f"{len(vectors)} vectors stored."

        )

    except Exception as e:

        logger.error(

            f"Pinecone Store Error : {e}"

        )


# ==========================================================
# Similarity Search
# ==========================================================

def similarity_search(

    query_embedding,

    top_k=5,

    filters=None

):

    """
    Search similar resume chunks.
    """

    try:

        response = index.query(

            vector=query_embedding,

            top_k=top_k,

            include_metadata=True,

            filter=filters

        )

        logger.info(

            "Similarity Search Completed"

        )

        return response.matches

    except Exception as e:

        logger.error(

            f"Search Error : {e}"

        )

        return []


# ==========================================================
# Fetch Vector
# ==========================================================

def fetch_vector(vector_id):

    """
    Fetch vector by ID.
    """

    try:

        result = index.fetch(

            ids=[vector_id]

        )

        return result

    except Exception as e:

        logger.error(

            f"Fetch Error : {e}"

        )

        return None


# ==========================================================
# Delete Vector
# ==========================================================

def delete_vector(vector_id):

    """
    Delete one vector.
    """

    try:

        index.delete(

            ids=[vector_id]

        )

        logger.info(

            f"Deleted : {vector_id}"

        )

    except Exception as e:

        logger.error(

            f"Delete Error : {e}"

        )


# ==========================================================
# Delete All Resume Vectors
# ==========================================================

def delete_resume_vectors(resume_id):

    """
    Delete all vectors for a resume.
    """

    try:

        index.delete(

            filter={

                "resume_id": resume_id

            }

        )

        logger.info(

            f"Deleted Resume : {resume_id}"

        )

    except Exception as e:

        logger.error(

            f"Delete Resume Error : {e}"

        )


# ==========================================================
# Index Statistics
# ==========================================================

def index_statistics():

    """
    Return Pinecone statistics.
    """

    return index.describe_index_stats()