# print(git code upload code)
# """
# FastAPI backend for Resume AI Builder.
#
# This file is the ONLY new backend file. It wraps the original,
# unmodified business logic (analysis.py, db.py, results.py, pdf.py)
# in a REST API so a React frontend can drive the same flow that the
# Streamlit app used to drive:
#
#   Home (upload + quick analysis)
#      -> Save to DB
#      -> Dashboard (run tasks one by one)
#      -> Task Status (see progress / history)
#      -> Exit / Final Summary
#
# None of the AI prompts, the Groq calls, or the PostgreSQL queries were
# changed - they are imported as-is from analysis.py / db.py / results.py.
# """
#
# import os
# from io import BytesIO
# from typing import List, Optional
#
# import logging
# from contextlib import asynccontextmanager
#
# from dotenv import load_dotenv
# load_dotenv()
#
# # analysis.py imports streamlit; its "missing ScriptRunContext" warnings are harmless noise
# for _name in ("streamlit", "streamlit.runtime", "streamlit.runtime.scriptrunner_utils.script_run_context"):
#     logging.getLogger(_name).setLevel(logging.ERROR)
#
# from fastapi import FastAPI, UploadFile, File, Form, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import StreamingResponse, JSONResponse
# from fastapi import Request
# from docx import Document
#
# # ---------------------------------------------------------------
# # Original, unmodified business logic
# # ---------------------------------------------------------------
# from analysis import (
#     profile,
#     cover_page,
#     skill_performance,
#     skill_gap,
#     resume_summary_func,
# )
#
# from db import save_uploaded_documents, get_connection
# from init_db import init_db
# from auth import router as auth_router, auth_middleware
#
# from results import (
#     save_or_update_result,
#     get_dashboard_summary,
#     get_all_results,
#     get_final_summary,
#     all_tasks_completed,
#     clear_results,
#     TASKS,
# )
#
# # ---------------------------------------------------------------
# # App setup
# # ---------------------------------------------------------------
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Create the database/tables automatically if they are missing
#     init_db()
#     yield
#
#
# app = FastAPI(title="Resume AI Builder API", lifespan=lifespan)
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # tighten this in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# @app.exception_handler(Exception)
# async def unhandled_exception_handler(request: Request, exc: Exception):
#     # Return the real error text so the React UI can show it
#     # (full traceback is still printed in the uvicorn terminal).
#     import traceback
#     traceback.print_exc()
#     return JSONResponse(
#         status_code=500,
#         content={"detail": f"{type(exc).__name__}: {exc}"},
#         headers={"Access-Control-Allow-Origin": "*"},
#     )
#
#
# # Login protection: every /api/* route except /api/auth/* and /api/health needs a token
# app.include_router(auth_router)
# app.middleware("http")(auth_middleware)
#
# TASK_FUNCTIONS = {
#     "Profile": profile,
#     "Cover Letter": cover_page,
#     "Skill Performance": skill_performance,
#     "Skill Gap": skill_gap,
# }
#
#
# # ---------------------------------------------------------------
# # Shim so FastAPI's UploadFile can be handed to the original
# # functions, which expect an object with .name and .getvalue()
# # (that's what Streamlit's UploadedFile looks like).
# # ---------------------------------------------------------------
# class FileShim:
#     def __init__(self, filename: str, data: bytes):
#         self.name = filename
#         self._buffer = BytesIO(data)
#
#     def getvalue(self):
#         return self._buffer.getvalue()
#
#     def read(self, *args, **kwargs):
#         return self._buffer.read(*args, **kwargs)
#
#     def seek(self, *args, **kwargs):
#         return self._buffer.seek(*args, **kwargs)
#
#     def tell(self):
#         return self._buffer.tell()
#
#
# async def to_shim(upload: Optional[UploadFile]) -> Optional[FileShim]:
#     if upload is None:
#         return None
#     data = await upload.read()
#     return FileShim(upload.filename, data)
#
#
# # ---------------------------------------------------------------
# # Health check
# # ---------------------------------------------------------------
# @app.get("/api/health")
# def health():
#     return {"status": "ok"}
#
#
# # ---------------------------------------------------------------
# # Home page: quick, un-saved AI features
# # (mirrors the "Get Insights / Generate Cover Letter / Analyze
# # Skills / Find Missing Skills" buttons in the original app.py)
# # ---------------------------------------------------------------
# @app.post("/api/analyze")
# async def analyze(
#     task: str = Form(...),  # "profile" | "cover" | "skill_performance" | "skill_gap"
#     job_desc: str = Form(...),
#     resume: UploadFile = File(...),
# ):
#     resume_shim = await to_shim(resume)
#
#     if task == "profile":
#         result = profile(resume=resume_shim, job_desc=job_desc)
#     elif task == "cover":
#         result = cover_page(resume=resume_shim, job_desc=job_desc)
#     elif task == "skill_performance":
#         result = skill_performance(resume=resume_shim, job_desc=job_desc)
#     elif task == "skill_gap":
#         result = skill_gap(resume=resume_shim, job_desc=job_desc)
#     else:
#         raise HTTPException(status_code=400, detail="Invalid task")
#
#     return {"task": task, "result": result}
#
#
# # ---------------------------------------------------------------
# # Cover letter -> .docx download (same python-docx logic as app.py)
# # ---------------------------------------------------------------
# print(git code upload code)
# @app.post("/api/cover-letter/docx")
# async def cover_letter_docx(text: str = Form(...)):
#     document = Document()
#     document.add_heading("Cover Letter", level=1)
#     document.add_paragraph(text)
#
#     buffer = BytesIO()
#     document.save(buffer)
#     buffer.seek(0)
#
#     return StreamingResponse(
#         buffer,
#         media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
#         headers={"Content-Disposition": "attachment; filename=Cover_Letter.docx"},
#     )
#
#
# # ---------------------------------------------------------------
# # Save resume + job description (+ optional certifications) to DB
# # (mirrors the sidebar "Save to Database" flow in app.py)
# # ---------------------------------------------------------------
# @app.post("/api/save-documents")
# async def save_documents(
#     job_desc: str = Form(...),
#     resume: UploadFile = File(...),
#     certifications: List[UploadFile] = File(default=[]),
# ):
#     resume_shim = await to_shim(resume)
#
#     cert_shims = []
#     for cert in certifications:
#         if cert is not None and cert.filename:
#             cert_shims.append(await to_shim(cert))
#
#     summary = resume_summary_func(resume_shim)
#
#     document_id = save_uploaded_documents(
#         resume_file=resume_shim,
#         job_description=job_desc,
#         certification_files=cert_shims,
#         resume_summary=summary,
#     )
#
#     return {"document_id": document_id, "resume_summary": summary}
#
#
# # ---------------------------------------------------------------
# # Dashboard summary
# # ---------------------------------------------------------------
# @app.get("/api/dashboard/{document_id}")
# def dashboard(document_id: int):
#     return get_dashboard_summary(document_id)
#
#
# # ---------------------------------------------------------------
# # Run a single task from the dashboard
# # (mirrors task_manager.execute_task, minus the Streamlit UI calls)
# # ---------------------------------------------------------------
# @app.post("/api/tasks/run")
# async def run_task(
#     document_id: int = Form(...),
#     task_name: str = Form(...),
#     job_desc: str = Form(...),
#     resume: UploadFile = File(...),
# ):
#     if task_name not in TASK_FUNCTIONS:
#         raise HTTPException(status_code=400, detail="Invalid task")
#
#     resume_shim = await to_shim(resume)
#
#     task_function = TASK_FUNCTIONS[task_name]
#     result = task_function(resume=resume_shim, job_desc=job_desc)
#
#     save_or_update_result(document_id, task_name, result)
#
#     summary = get_dashboard_summary(document_id)
#
#     return {
#         "task_name": task_name,
#         "result": result,
#         "summary": summary,
#         "all_completed": all_tasks_completed(document_id),
#     }
#
#
# # ---------------------------------------------------------------
# # Task status page
# # ---------------------------------------------------------------
# @app.get("/api/status/{document_id}")
# def status(document_id: int):
#     summary = get_dashboard_summary(document_id)
#
#     rows = get_all_results(document_id)
#     history = [
#         {
#             "task_name": r[0],
#             "generated_result": r[1],
#             "task_status": r[2],
#             "completed": r[3],
#             "execution_time": r[4].isoformat() if r[4] else None,
#         }
#         for r in rows
#     ]
#
#     return {**summary, "history": history}
#
#
# # ---------------------------------------------------------------
# # Exit / final summary page
# # ---------------------------------------------------------------
# @app.get("/api/exit/{document_id}")
# def exit_page(document_id: int):
#     summary = get_dashboard_summary(document_id)
#     final = get_final_summary(document_id)
#
#     results = [
#         {
#             "task_name": r[0],
#             "generated_result": r[1],
#             "task_status": r[2],
#             "completed": r[3],
#             "execution_time": r[4].isoformat() if r[4] else None,
#         }
#         for r in final["results"]
#     ]
#
#     return {
#         **summary,
#         "results": results,
#         "all_completed": all_tasks_completed(document_id),
#     }
#
#
# # ---------------------------------------------------------------
# # Reset / start over
# # ---------------------------------------------------------------
# @app.post("/api/reset/{document_id}")
# def reset(document_id: int):
#     clear_results(document_id)
#     return {"status": "cleared"}
#
#
# # ---------------------------------------------------------------
# # Rating + feedback (shown when the user exits)
# # ---------------------------------------------------------------
# @app.post("/api/feedback")
# def submit_feedback(
#     rating: int = Form(...),
#     comments: str = Form(""),
#     document_id: Optional[int] = Form(None),
# ):
#     if rating < 1 or rating > 5:
#         raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
#
#     conn = get_connection()
#     cursor = conn.cursor()
#     try:
#         cursor.execute(
#             "INSERT INTO feedback (document_id, rating, comments) VALUES (%s, %s, %s)",
#             (document_id, rating, comments.strip() or None),
#         )
#         conn.commit()
#     except Exception:
#         conn.rollback()
#         raise
#     finally:
#         cursor.close()
#         conn.close()
#
#     return {"status": "saved"}
#
#
# @app.get("/api/tasks")
# def list_tasks():
#     return {"tasks": TASKS}
#

# print(git code upload code)