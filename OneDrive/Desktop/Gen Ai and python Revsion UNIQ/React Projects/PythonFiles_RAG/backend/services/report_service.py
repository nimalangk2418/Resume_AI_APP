"""
services/report_service.py

Resume Screening Report Service

Responsibilities
----------------
1. Store AI Screening Result
2. Generate JSON Report
3. Generate PDF Report
4. Save Report Information
"""

import os
import json

from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.database.models import (
    ScreeningResult,
    Report
)

from PythonFiles_RAG.backend.utils.config import settings
from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Create Report Folder
# ==========================================================

os.makedirs(

    settings.REPORT_FOLDER,

    exist_ok=True

)


# ==========================================================
# Store Screening Result
# ==========================================================

def save_screening_result(

    resume_id: int,

    job_id: int,

    result: dict,

    db: Session

):

    screening = ScreeningResult(

        resume_id=resume_id,

        job_id=job_id,

        match_score=float(

            result.get(

                "match_score",

                0

            )

        ),

        recommendation=result.get(

            "recommendation",

            ""

        ),

        skill_gap=json.dumps(

            result.get(

                "skill_gap",

                []

            )

        ),

        interview_questions=json.dumps(

            result.get(

                "interview_questions",

                []

            )

        )

    )

    db.add(screening)

    db.commit()

    db.refresh(screening)

    logger.info("Screening Result Saved")

    return screening


# ==========================================================
# Generate PDF Report
# ==========================================================

def generate_pdf(

    screening,

    result

):

    report_name = (

        f"screening_"

        f"{screening.screening_id}.pdf"

    )

    report_path = os.path.join(

        settings.REPORT_FOLDER,

        report_name

    )

    document = SimpleDocTemplate(

        report_path

    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(

        Paragraph(

            "<b>Resume AI Screening Report</b>",

            styles["Heading1"]

        )

    )

    elements.append(

        Paragraph(

            f"<b>Candidate:</b> "

            f"{result.get('candidate_name','N/A')}",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            f"<b>Match Score:</b> "

            f"{result.get('match_score','0')}%",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            f"<b>Recommendation:</b><br/>"

            f"{result.get('recommendation','')}",

            styles["BodyText"]

        )

    )

    elements.append(

        Paragraph(

            "<b>Technical Skills</b>",

            styles["Heading2"]

        )

    )

    for skill in result.get(

        "technical_skills",

        []

    ):

        elements.append(

            Paragraph(

                f"• {skill}",

                styles["BodyText"]

            )

        )

    elements.append(

        Paragraph(

            "<b>Skill Gap</b>",

            styles["Heading2"]

        )

    )

    for skill in result.get(

        "skill_gap",

        []

    ):

        elements.append(

            Paragraph(

                f"• {skill}",

                styles["BodyText"]

            )

        )

    elements.append(

        Paragraph(

            "<b>Interview Questions</b>",

            styles["Heading2"]

        )

    )

    for question in result.get(

        "interview_questions",

        []

    ):

        elements.append(

            Paragraph(

                f"• {question}",

                styles["BodyText"]

            )

        )

    document.build(elements)

    return report_name, report_path


# ==========================================================
# Save Report Information
# ==========================================================

def save_report(

    screening,

    report_name,

    report_path,

    db: Session

):

    report = Report(

        screening_id=screening.screening_id,

        report_name=report_name,

        report_path=report_path

    )

    db.add(report)

    db.commit()

    db.refresh(report)

    logger.info("Report Saved")

    return report


# ==========================================================
# Complete Report Pipeline
# ==========================================================

def generate_screening_report(

    resume_id: int,

    job_id: int,

    result: dict,

    db: Session

):

    logger.info("Generating Report")

    screening = save_screening_result(

        resume_id,

        job_id,

        result,

        db

    )

    report_name, report_path = generate_pdf(

        screening,

        result

    )

    report = save_report(

        screening,

        report_name,

        report_path,

        db

    )

    logger.info("Report Generation Completed")

    return {

        "screening_id": screening.screening_id,

        "report_id": report.report_id,

        "report_name": report_name,

        "report_path": report_path

    }