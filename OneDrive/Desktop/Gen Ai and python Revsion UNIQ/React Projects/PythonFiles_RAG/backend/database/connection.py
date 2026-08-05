"""
database/connection.py

Database Connection Module
--------------------------
Creates the PostgreSQL database connection,
SQLAlchemy engine, session factory,
and Base model for ORM.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from PythonFiles_RAG.backend.utils.config import settings


# ==========================================================
# Database URL
# ==========================================================

DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)


# ==========================================================
# SQLAlchemy Engine
# ==========================================================

engine = create_engine(
    DATABASE_URL,

    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,

    echo=False
)


# ==========================================================
# Session Factory
# ==========================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==========================================================
# Base Class
# ==========================================================

Base = declarative_base()


# ==========================================================
# Dependency
# ==========================================================

def get_db():

    """
    Returns a database session.
    Automatically closes after request.
    """

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# ==========================================================
# Create Tables
# ==========================================================

def create_database():

    """
    Creates all database tables.
    """

    Base.metadata.create_all(bind=engine)


# ==========================================================
# Database Health Check
# ==========================================================

def check_database():

    """
    Returns True if database connection is successful.
    """

    try:

        connection = engine.connect()

        connection.close()

        return True

    except Exception as e:

        print("Database Error :", e)

        return False