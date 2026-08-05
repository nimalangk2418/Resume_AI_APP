"""
api/upload.py

Resume & Job Description Upload API
"""

import os
import shutil
from datetime import datetime

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.database.connection import get_db
from PythonFiles_RAG.backend.database.models import Resume, JobDescription

from PythonFiles_RAG.backend.utils.config import settings
from PythonFiles_RAG.backend.utils.logger import logger

from PythonFiles_RAG.backend.services.document_processor import process_document

# ==========================================================
# Router
# ==========================================================

router = APIRouter()

# ==========================================================
# Create Upload Directory
# ==========================================================

os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

# ==========================================================
# Allowed File Types
# ==========================================================

ALLOWED_EXTENSIONS = [".pdf", ".docx"]

# ==========================================================
# Upload Resume
# ==========================================================

@router.post("/resume")

async def upload_resume(

    file: UploadFile = File(...),

    db: Session = Depends(get_db)

):

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(

            status_code=400,

            detail="Only PDF and DOCX files are allowed."

        )

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    filename = f"{timestamp}_{file.filename}"

    filepath = os.path.join(

        settings.UPLOAD_FOLDER,

        filename

    )

    with open(filepath, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    resume = Resume(

        file_name=filename,

        file_path=filepath,

        processing_status="Uploaded"

    )

    db.add(resume)

    db.commit()

    db.refresh(resume)

    logger.info(

        f"Resume Uploaded : {filename}"

    )

    # Start Resume Processing

    process_document(

        resume.resume_id,

        filepath,

        db

    )

    return {

        "message": "Resume uploaded successfully.",

        "resume_id": resume.resume_id,

        "file_name": filename

    }


# ==========================================================
# Upload Job Description
# ==========================================================

@router.post("/job-description")

async def upload_job_description(

    job_title: str,

    company_name: str,

    description: str,

    required_skills: str,

    experience: str,

    db: Session = Depends(get_db)

):

    job = JobDescription(

        job_title=job_title,

        company_name=company_name,

        description=description,

        required_skills=required_skills,

        experience=experience

    )

    db.add(job)

    db.commit()

    db.refresh(job)

    logger.info(

        f"Job Description Uploaded : {job.job_title}"

    )

    return {

        "message": "Job Description uploaded successfully.",

        "job_id": job.job_id

    }


# ==========================================================
# Get Uploaded Resumes
# ==========================================================

@router.get("/resumes")

def get_uploaded_resumes(

    db: Session = Depends(get_db)

):

    resumes = db.query(Resume).all()

    return resumes


# ==========================================================
# Get Uploaded Job Descriptions
# ==========================================================

@router.get("/job-descriptions")

def get_job_descriptions(

    db: Session = Depends(get_db)

):

    jobs = db.query(JobDescription).all()

    return jobs