"""
services/chunk_service.py

Semantic Chunking Service

Responsibilities
----------------
1. Split resume into semantic sections
2. Create meaningful chunks
3. Store chunks in PostgreSQL
4. Return chunks for embedding generation
"""

import re

from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.database.models import SemanticChunk

from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Resume Section Keywords
# ==========================================================

SECTION_HEADERS = [

    "summary",
    "professional summary",

    "skills",
    "technical skills",
    "technical competencies",

    "experience",
    "work experience",
    "employment history",

    "projects",

    "education",

    "certifications",

    "achievements",

    "publications"

]


# ==========================================================
# Split Resume into Sections
# ==========================================================

def split_into_sections(text: str):

    """
    Split resume into semantic sections
    """

    sections = {}

    current_section = "General"

    sections[current_section] = ""

    for line in text.split("."):

        line = line.strip()

        lower_line = line.lower()

        matched = False

        for header in SECTION_HEADERS:

            if header in lower_line:

                current_section = header.title()

                sections[current_section] = ""

                matched = True

                break

        if not matched:

            sections[current_section] += line + ". "

    return sections


# ==========================================================
# Create Semantic Chunks
# ==========================================================

def create_semantic_chunks(

    resume_id: int,

    text: str,

    db: Session

):

    """
    Creates semantic chunks and stores them
    """

    logger.info("Semantic Chunking Started")

    sections = split_into_sections(text)

    chunks = []

    order = 1

    for section_name, content in sections.items():

        content = content.strip()

        if len(content) == 0:

            continue

        chunk = SemanticChunk(

            resume_id=resume_id,

            section_name=section_name,

            chunk_text=content,

            chunk_order=order

        )

        db.add(chunk)

        chunks.append({

            "section": section_name,

            "text": content

        })

        order += 1

    db.commit()

    logger.info(f"{len(chunks)} Semantic Chunks Created")

    return chunks