"""
database/models.py

SQLAlchemy ORM Models
Resume AI Screening Assistant
Hybrid RAG Architecture
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from PythonFiles_RAG.backend.database.connection import Base


# ==========================================================
# Recruiter Table
# ==========================================================

class Recruiter(Base):

    __tablename__ = "recruiters"

    recruiter_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), default="Recruiter")
    created_at = Column(DateTime, default=datetime.utcnow)


# ==========================================================
# Job Description Table
# ==========================================================

class JobDescription(Base):

    __tablename__ = "job_descriptions"

    job_id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String(150), nullable=False)
    company_name = Column(String(150))
    description = Column(Text)
    required_skills = Column(Text)
    experience = Column(String(50))
    uploaded_at = Column(DateTime, default=datetime.utcnow)


# ==========================================================
# Resume Table
# ==========================================================

class Resume(Base):

    __tablename__ = "resumes"

    resume_id = Column(Integer, primary_key=True, index=True)
    candidate_name = Column(String(150))
    email = Column(String(150))
    phone = Column(String(20))
    file_name = Column(String(255))
    file_path = Column(String(500))
    upload_time = Column(DateTime, default=datetime.utcnow)
    processing_status = Column(String(50), default="Uploaded")

    metadata = relationship(
        "ResumeMetadata",
        back_populates="resume",
        cascade="all, delete"
    )

    chunks = relationship(
        "SemanticChunk",
        back_populates="resume",
        cascade="all, delete"
    )

    screening_results = relationship(
        "ScreeningResult",
        back_populates="resume",
        cascade="all, delete"
    )


# ==========================================================
# Resume Metadata Table
# ==========================================================

class ResumeMetadata(Base):

    __tablename__ = "resume_metadata"

    metadata_id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(
        Integer,
        ForeignKey("resumes.resume_id"),
        nullable=False
    )

    skills = Column(Text)
    education = Column(Text)
    experience = Column(Text)
    certifications = Column(Text)
    projects = Column(Text)
    location = Column(String(100))
    total_experience = Column(Float)

    resume = relationship(
        "Resume",
        back_populates="metadata"
    )


# ==========================================================
# Semantic Chunks Table
# ==========================================================

class SemanticChunk(Base):

    __tablename__ = "semantic_chunks"

    chunk_id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(
        Integer,
        ForeignKey("resumes.resume_id"),
        nullable=False
    )

    section_name = Column(String(100))
    chunk_text = Column(Text)
    chunk_order = Column(Integer)

    resume = relationship(
        "Resume",
        back_populates="chunks"
    )


# ==========================================================
# Screening Results Table
# ==========================================================

class ScreeningResult(Base):

    __tablename__ = "screening_results"

    screening_id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(
        Integer,
        ForeignKey("resumes.resume_id"),
        nullable=False
    )

    job_id = Column(
        Integer,
        ForeignKey("job_descriptions.job_id"),
        nullable=False
    )

    match_score = Column(Float)
    recommendation = Column(Text)
    skill_gap = Column(Text)
    interview_questions = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    resume = relationship(
        "Resume",
        back_populates="screening_results"
    )

    job = relationship("JobDescription")

    reports = relationship(
        "Report",
        back_populates="screening_result",
        cascade="all, delete"
    )


# ==========================================================
# Reports Table
# ==========================================================

class Report(Base):

    __tablename__ = "reports"

    report_id = Column(Integer, primary_key=True, index=True)

    screening_id = Column(
        Integer,
        ForeignKey("screening_results.screening_id"),
        nullable=False
    )

    report_name = Column(String(200))
    report_path = Column(String(500))

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    screening_result = relationship(
        "ScreeningResult",
        back_populates="reports"
    )