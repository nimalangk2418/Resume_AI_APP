"""
api/screening.py

Hybrid RAG Resume Screening API
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.database.connection import get_db
from PythonFiles_RAG.backend.database.models import ResumeMetadata

from PythonFiles_RAG.backend.services.retriever import retrieve_documents
from PythonFiles_RAG.backend.services.reranker import rerank_documents
from PythonFiles_RAG.backend.services.prompt_builder import build_prompt
from PythonFiles_RAG.backend.services.llm_service import screen_candidate
from PythonFiles_RAG.backend.services.report_service import generate_screening_report

from PythonFiles_RAG.backend.utils.logger import logger

router = APIRouter()


# ==========================================================
# Resume Screening API
# ==========================================================

@router.post("/candidate")

def screen_resume(

    resume_id: int,

    job_id: int,

    recruiter_query: str,

    job_description: str,

    db: Session = Depends(get_db)

):

    logger.info("Resume Screening Started")

    # -----------------------------------------
    # Load Candidate Metadata
    # -----------------------------------------

    metadata = db.query(ResumeMetadata).filter(

        ResumeMetadata.resume_id == resume_id

    ).first()

    if metadata is None:

        raise HTTPException(

            status_code=404,

            detail="Resume Metadata Not Found"

        )

    metadata_dict = {

        "skills": metadata.skills,

        "education": metadata.education,

        "experience": metadata.experience,

        "certifications": metadata.certifications,

        "projects": metadata.projects

    }

    # -----------------------------------------
    # Retrieve Resume Chunks
    # -----------------------------------------

    retrieved_documents = retrieve_documents(

        query=recruiter_query,

        top_k=10

    )

    if len(retrieved_documents) == 0:

        raise HTTPException(

            status_code=404,

            detail="No Resume Chunks Retrieved"

        )

    # -----------------------------------------
    # Cross Encoder Reranking
    # -----------------------------------------

    reranked_documents = rerank_documents(

        recruiter_query,

        retrieved_documents,

        top_k=5

    )

    # -----------------------------------------
    # Build Prompt
    # -----------------------------------------

    prompt = build_prompt(

        recruiter_query,

        job_description,

        metadata_dict,

        reranked_documents

    )

    # -----------------------------------------
    # Groq Screening
    # -----------------------------------------

    ai_result = screen_candidate(

        prompt

    )

    # -----------------------------------------
    # Generate Report
    # -----------------------------------------

    report = generate_screening_report(

        resume_id,

        job_id,

        ai_result,

        db

    )

    logger.info("Resume Screening Completed")

    return {

        "status": "Success",

        "screening_result": ai_result,

        "report": report

    }


# ==========================================================
# Compare Candidates
# ==========================================================

@router.post("/compare")

def compare_candidates(

    query: str,

    db: Session = Depends(get_db)

):

    documents = retrieve_documents(

        query=query,

        top_k=10

    )

    documents = rerank_documents(

        query,

        documents,

        top_k=5

    )

    return {

        "candidates": documents

    }