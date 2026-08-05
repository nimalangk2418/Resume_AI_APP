"""
services/metadata_service.py

Resume Metadata Extraction Service

Responsibilities
----------------
1. Extract candidate metadata
2. Store metadata in PostgreSQL
3. Return extracted metadata
"""

import re

from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.database.models import ResumeMetadata

from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Helper Functions
# ==========================================================

def extract_email(text: str):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:

        return match.group()

    return ""


def extract_phone(text: str):

    pattern = r"(\+91[- ]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:

        return match.group()

    return ""


# ==========================================================
# Skill Extraction
# ==========================================================

SKILLS = [

    "Python",
    "Java",
    "SQL",
    "FastAPI",
    "Flask",
    "React",
    "JavaScript",
    "HTML",
    "CSS",
    "AWS",
    "Azure",
    "Docker",
    "Kubernetes",
    "LangChain",
    "LangGraph",
    "Pinecone",
    "PostgreSQL",
    "Machine Learning",
    "Deep Learning",
    "Power BI",
    "TensorFlow",
    "PyTorch"

]


def extract_skills(text):

    found = []

    lower_text = text.lower()

    for skill in SKILLS:

        if skill.lower() in lower_text:

            found.append(skill)

    return list(set(found))


# ==========================================================
# Education Extraction
# ==========================================================

EDUCATION = [

    "Bachelor",

    "B.Tech",

    "B.E",

    "Master",

    "M.Tech",

    "MBA",

    "PhD"

]


def extract_education(text):

    education = []

    lower = text.lower()

    for degree in EDUCATION:

        if degree.lower() in lower:

            education.append(degree)

    return education


# ==========================================================
# Certification Extraction
# ==========================================================

CERTIFICATIONS = [

    "AWS",

    "Azure",

    "Google Cloud",

    "Databricks",

    "Microsoft",

    "Oracle",

    "Cisco"

]


def extract_certifications(text):

    result = []

    lower = text.lower()

    for cert in CERTIFICATIONS:

        if cert.lower() in lower:

            result.append(cert)

    return result


# ==========================================================
# Experience Extraction
# ==========================================================

def extract_experience(text):

    pattern = r"(\d+)\+?\s*(years|year|months|month)"

    matches = re.findall(pattern, text, re.IGNORECASE)

    experience = []

    for match in matches:

        experience.append(" ".join(match))

    return experience


# ==========================================================
# Projects Extraction
# ==========================================================

PROJECT_HEADERS = [

    "project",

    "projects",

    "academic project",

    "professional project"

]


def extract_projects(text):

    projects = []

    sentences = text.split(".")

    for sentence in sentences:

        for keyword in PROJECT_HEADERS:

            if keyword.lower() in sentence.lower():

                projects.append(sentence.strip())

                break

    return projects


# ==========================================================
# Main Metadata Extraction
# ==========================================================

def extract_metadata(

    resume_id: int,

    text: str,

    db: Session

):

    logger.info("Metadata Extraction Started")

    skills = extract_skills(text)

    education = extract_education(text)

    certifications = extract_certifications(text)

    experience = extract_experience(text)

    projects = extract_projects(text)

    metadata = ResumeMetadata(

        resume_id=resume_id,

        skills=", ".join(skills),

        education=", ".join(education),

        experience=", ".join(experience),

        certifications=", ".join(certifications),

        projects="\n".join(projects),

        total_experience=0

    )

    db.add(metadata)

    db.commit()

    db.refresh(metadata)

    logger.info("Metadata Extraction Completed")

    return {

        "skills": skills,

        "education": education,

        "certifications": certifications,

        "experience": experience,

        "projects": projects

    }