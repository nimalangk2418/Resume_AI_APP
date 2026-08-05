"""
services/document_processor.py

Resume Document Processing Service
Hybrid RAG Resume Screening Assistant

Responsibilities
----------------
1. Read uploaded Resume (PDF/DOCX)
2. Perform OCR for scanned PDFs
3. Extract Resume Text
4. Clean Extracted Text
5. Update Resume Status
6. Extract Resume Metadata
7. Perform Semantic Chunking
8. Generate Embeddings
"""

import os

import fitz
from docx import Document
from PIL import Image
import pytesseract

from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.database.models import Resume

from PythonFiles_RAG.backend.utils.logger import logger

from PythonFiles_RAG.backend.services.chunk_service import create_semantic_chunks
from PythonFiles_RAG.backend.services.metadata_service import extract_metadata
from PythonFiles_RAG.backend.services.embedding_service import generate_embeddings


# ==========================================================
# PDF TEXT EXTRACTION
# ==========================================================

def extract_pdf_text(file_path: str):

    """
    Extract text from digital PDF
    """

    text = ""

    try:

        pdf = fitz.open(file_path)

        for page in pdf:

            text += page.get_text()

        pdf.close()

    except Exception as e:

        logger.error(f"PDF Extraction Error : {e}")

    return text


# ==========================================================
# OCR FOR SCANNED PDF
# ==========================================================

def extract_text_using_ocr(file_path: str):

    """
    Extract text from scanned PDF using OCR
    """

    text = ""

    try:

        pdf = fitz.open(file_path)

        for page in pdf:

            pix = page.get_pixmap()

            image_path = "temp_page.png"

            pix.save(image_path)

            image = Image.open(image_path)

            text += pytesseract.image_to_string(image)

            os.remove(image_path)

        pdf.close()

    except Exception as e:

        logger.error(f"OCR Error : {e}")

    return text


# ==========================================================
# DOCX TEXT EXTRACTION
# ==========================================================

def extract_docx_text(file_path: str):

    """
    Read DOCX Resume
    """

    text = ""

    try:

        document = Document(file_path)

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

    except Exception as e:

        logger.error(f"DOCX Extraction Error : {e}")

    return text


# ==========================================================
# TEXT CLEANING
# ==========================================================

def clean_text(text: str):

    """
    Clean extracted resume text
    """

    text = text.replace("\n", " ")

    text = text.replace("\t", " ")

    text = " ".join(text.split())

    return text


# ==========================================================
# MAIN DOCUMENT PROCESSING PIPELINE
# ==========================================================

def process_document(

    resume_id: int,

    file_path: str,

    db: Session

):

    logger.info("===================================")
    logger.info("Resume Processing Started")
    logger.info("===================================")

    extension = os.path.splitext(file_path)[1].lower()

    # ------------------------------------------------------
    # STEP 1 : Read Resume
    # ------------------------------------------------------

    if extension == ".pdf":

        logger.info("Reading PDF Resume...")

        text = extract_pdf_text(file_path)

        # If extracted text is too small,
        # assume scanned PDF

        if len(text.strip()) < 100:

            logger.info("Scanned Resume Detected")

            logger.info("Performing OCR...")

            text = extract_text_using_ocr(file_path)

    elif extension == ".docx":

        logger.info("Reading DOCX Resume...")

        text = extract_docx_text(file_path)

    else:

        raise Exception("Unsupported Resume Format")



    # ------------------------------------------------------
    # STEP 2 : Clean Resume Text
    # ------------------------------------------------------

    logger.info("Cleaning Resume Text...")

    text = clean_text(text)



    # ------------------------------------------------------
    # STEP 3 : Update Resume Status
    # ------------------------------------------------------

    resume = db.query(Resume).filter(

        Resume.resume_id == resume_id

    ).first()

    resume.processing_status = "Processing"

    db.commit()



    # ------------------------------------------------------
    # STEP 4 : Metadata Extraction
    # ------------------------------------------------------

    logger.info("Extracting Resume Metadata...")

    metadata = extract_metadata(

        resume_id,

        text,

        db

    )



    # ------------------------------------------------------
    # STEP 5 : Semantic Chunking
    # ------------------------------------------------------

    logger.info("Creating Semantic Chunks...")

    chunks = create_semantic_chunks(

        resume_id,

        text,

        db

    )



    # ------------------------------------------------------
    # STEP 6 : Embedding Generation
    # ------------------------------------------------------

    logger.info("Generating Embeddings...")

    generate_embeddings(

        resume_id,

        chunks,

        db

    )



    # ------------------------------------------------------
    # STEP 7 : Processing Completed
    # ------------------------------------------------------

    resume.processing_status = "Completed"

    db.commit()

    logger.info("===================================")
    logger.info("Resume Processing Completed")
    logger.info("===================================")

    return {

        "resume_id": resume_id,

        "status": "Completed",

        "metadata_extracted": True,

        "semantic_chunks": len(chunks)

    }