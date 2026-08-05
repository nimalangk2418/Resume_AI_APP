"""
api/report.py

Resume Screening Report API
"""

import os

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from PythonFiles_RAG.backend.database.connection import get_db
from PythonFiles_RAG.backend.database.models import (
    Report,
    ScreeningResult
)

from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Router
# ==========================================================

router = APIRouter()


# ==========================================================
# Get All Reports
# ==========================================================

@router.get("/all")

def get_all_reports(

    db: Session = Depends(get_db)

):

    reports = db.query(Report).all()

    return reports


# ==========================================================
# Get Report by ID
# ==========================================================

@router.get("/{report_id}")

def get_report(

    report_id: int,

    db: Session = Depends(get_db)

):

    report = db.query(Report).filter(

        Report.report_id == report_id

    ).first()

    if report is None:

        raise HTTPException(

            status_code=404,

            detail="Report Not Found"

        )

    return report


# ==========================================================
# Download Report
# ==========================================================

@router.get("/download/{report_id}")

def download_report(

    report_id: int,

    db: Session = Depends(get_db)

):

    report = db.query(Report).filter(

        Report.report_id == report_id

    ).first()

    if report is None:

        raise HTTPException(

            status_code=404,

            detail="Report Not Found"

        )

    if not os.path.exists(report.report_path):

        raise HTTPException(

            status_code=404,

            detail="PDF File Not Found"

        )

    logger.info(

        f"Downloading Report : {report.report_name}"

    )

    return FileResponse(

        path=report.report_path,

        filename=report.report_name,

        media_type="application/pdf"

    )


# ==========================================================
# Screening History
# ==========================================================

@router.get("/history/{resume_id}")

def screening_history(

    resume_id: int,

    db: Session = Depends(get_db)

):

    history = db.query(

        ScreeningResult

    ).filter(

        ScreeningResult.resume_id == resume_id

    ).all()

    return history


# ==========================================================
# Delete Report
# ==========================================================

@router.delete("/{report_id}")

def delete_report(

    report_id: int,

    db: Session = Depends(get_db)

):

    report = db.query(Report).filter(

        Report.report_id == report_id

    ).first()

    if report is None:

        raise HTTPException(

            status_code=404,

            detail="Report Not Found"

        )

    if os.path.exists(report.report_path):

        os.remove(report.report_path)

    db.delete(report)

    db.commit()

    logger.info(

        f"Report Deleted : {report_id}"

    )

    return {

        "message": "Report Deleted Successfully"

    }