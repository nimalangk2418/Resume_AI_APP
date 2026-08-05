"""
utils/config.py

Application Configuration
Loads all environment variables from .env
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # =====================================================
    # FastAPI
    # =====================================================

    PROJECT_NAME: str = "Resume AI Screening Assistant"

    VERSION: str = "1.0.0"

    DEBUG: bool = True


    # =====================================================
    # PostgreSQL
    # =====================================================

    DB_HOST: str

    DB_PORT: int

    DB_NAME: str

    DB_USER: str

    DB_PASSWORD: str


    # =====================================================
    # JWT Authentication
    # =====================================================

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


    # =====================================================
    # Groq API
    # =====================================================

    GROQ_API_KEY: str

    GROQ_MODEL: str = "llama-3.3-70b-versatile"


    # =====================================================
    # Pinecone
    # =====================================================

    PINECONE_API_KEY: str

    PINECONE_INDEX: str


    # =====================================================
    # Embedding Model
    # =====================================================

    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"


    # =====================================================
    # Redis
    # =====================================================

    REDIS_URL: str


    # =====================================================
    # File Upload
    # =====================================================

    UPLOAD_FOLDER: str = "uploads"

    MAX_FILE_SIZE: int = 10485760      # 10 MB


    # =====================================================
    # Report Folder
    # =====================================================

    REPORT_FOLDER: str = "reports"


    class Config:

        env_file = ".env"

        case_sensitive = True


settings = Settings()