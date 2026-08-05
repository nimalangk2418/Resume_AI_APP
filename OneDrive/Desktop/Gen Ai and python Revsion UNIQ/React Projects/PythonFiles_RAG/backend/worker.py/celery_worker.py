"""
workers/celery_worker.py

Background Task Worker
Resume AI Screening Assistant
"""

from celery import Celery

from PythonFiles_RAG.backend.utils.config import settings

from PythonFiles_RAG.backend.utils.logger import logger

from PythonFiles_RAG.backend.database.connection import SessionLocal

from PythonFiles_RAG.backend.services.document_processor import process_document



# ==========================================================
# Celery Configuration
# ==========================================================

celery_app = Celery(

    "resume_ai",

    broker=settings.REDIS_URL,

    backend=settings.REDIS_URL

)



celery_app.conf.update(

    task_serializer="json",

    accept_content=["json"],

    result_serializer="json",

    timezone="Asia/Kolkata",

    enable_utc=False

)



# ==========================================================
# Background Resume Processing
# ==========================================================

@celery_app.task

def process_resume(

    resume_id,

    file_path

):

    logger.info(

        f"Background Processing Started : {resume_id}"

    )

    db = SessionLocal()

    try:

        result = process_document(

            resume_id,

            file_path,

            db

        )

        logger.info(

            "Background Processing Completed"

        )

        return result

    except Exception as e:

        logger.error(

            f"Celery Error : {e}"

        )

        return None

    finally:

        db.close()



# ==========================================================
# Background Screening
# ==========================================================

@celery_app.task

def screen_resume(

    screening_function,

    *args,

    **kwargs

):

    logger.info(

        "AI Screening Started"

    )

    result = screening_function(

        *args,

        **kwargs

    )

    logger.info(

        "AI Screening Completed"

    )

    return result