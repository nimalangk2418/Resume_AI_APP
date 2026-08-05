"""
services/reranker.py

Cross Encoder Reranking Service

Responsibilities
----------------
1. Receive Retrieved Resume Chunks
2. Compute CrossEncoder Scores
3. Rerank Resume Chunks
4. Return Top Relevant Chunks
"""

from sentence_transformers import CrossEncoder

from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Load CrossEncoder Model
# ==========================================================

reranker_model = CrossEncoder(

    "cross-encoder/ms-marco-MiniLM-L-6-v2"

)


# ==========================================================
# Rerank Retrieved Documents
# ==========================================================

def rerank_documents(

    query: str,

    documents: list,

    top_k: int = 5

):

    """
    Rerank retrieved resume chunks.
    """

    logger.info("Cross Encoder Reranking Started")

    if len(documents) == 0:

        return []

    sentence_pairs = [

        (

            query,

            document["text"]

        )

        for document in documents

    ]

    scores = reranker_model.predict(

        sentence_pairs

    )

    reranked_documents = []

    for document, score in zip(documents, scores):

        document["rerank_score"] = float(score)

        reranked_documents.append(document)

    reranked_documents.sort(

        key=lambda x: x["rerank_score"],

        reverse=True

    )

    logger.info(

        f"{len(reranked_documents)} Resume Chunks Reranked"

    )

    return reranked_documents[:top_k]


# ==========================================================
# Best Resume Chunk
# ==========================================================

def get_best_document(

    query: str,

    documents: list

):

    results = rerank_documents(

        query,

        documents,

        top_k=1

    )

    if len(results) == 0:

        return None

    return results[0]


# ==========================================================
# Top Resume Chunks
# ==========================================================

def get_top_documents(

    query: str,

    documents: list,

    top_k: int = 5

):

    return rerank_documents(

        query,

        documents,

        top_k

    )