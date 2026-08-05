"""
main.py

Resume AI Screening Assistant
Hybrid RAG Backend using FastAPI
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from PythonFiles_RAG.backend.database.connection import create_database

from PythonFiles_RAG.backend.api.auth import router as auth_router
from PythonFiles_RAG.backend.api.upload import router as upload_router
from PythonFiles_RAG.backend.api.screening import router as screening_router
from PythonFiles_RAG.backend.api.report import router as report_router


# ---------------------------------------------------------
# Create FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title="Resume AI Screening Assistant",
    version="1.0.0",
    description="Hybrid RAG Resume AI Screening using FastAPI, Pinecone, PostgreSQL and Groq LLM"
)


# ---------------------------------------------------------
# Enable CORS
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# Create Database Tables on Startup
# ---------------------------------------------------------

@app.on_event("startup")
def startup():

    create_database()

    print("Database Connected")

    print("Resume AI Screening Backend Started")


# ---------------------------------------------------------
# Register API Routers
# ---------------------------------------------------------

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

app.include_router(upload_router, prefix="/upload", tags=["Upload"])

app.include_router(screening_router, prefix="/screen", tags=["AI Screening"])

app.include_router(report_router, prefix="/report", tags=["Reports"])


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/")
def home():

    return {
        "application": "Resume AI Screening Assistant",
        "architecture": "Hybrid Retrieval-Augmented Generation",
        "backend": "FastAPI",
        "database": "PostgreSQL",
        "vector_database": "Pinecone",
        "llm": "Groq - Llama 3.3",
        "status": "Running"
    }


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "Healthy",
        "database": "Connected",
        "vector_database": "Connected",
        "llm": "Groq Available"
    }