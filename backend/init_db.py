# print(git code upload code)
# """
# Creates the PostgreSQL database and tables if they don't exist yet.
# Safe to run on every startup (everything is IF NOT EXISTS).
# Uses the same DB_* values from .env that db.py uses. db.py is untouched.
# """
# import os
# import psycopg2
# from psycopg2 import sql
#
# SCHEMA_STATEMENTS = [
#     """
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         username VARCHAR(50) UNIQUE NOT NULL,
#         full_name VARCHAR(100),
#         email VARCHAR(255) NOT NULL,
#         mobile VARCHAR(25),
#         password_hash TEXT NOT NULL,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         login_count INT NOT NULL DEFAULT 0,
#         last_login_at TIMESTAMPTZ
#     )
#     """,
#     "ALTER TABLE users ADD COLUMN IF NOT EXISTS full_name VARCHAR(100)",
#     "ALTER TABLE users ADD COLUMN IF NOT EXISTS mobile VARCHAR(25)",
#     "ALTER TABLE users ADD COLUMN IF NOT EXISTS login_count INT NOT NULL DEFAULT 0",
#     "ALTER TABLE users ADD COLUMN IF NOT EXISTS last_login_at TIMESTAMPTZ",
#     """
#     CREATE TABLE IF NOT EXISTS uploaded_documents (
#         id SERIAL PRIMARY KEY,
#         resume_name VARCHAR(255),
#         resume_file BYTEA,
#         job_description TEXT,
#         resume_summary TEXT,
#         uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     )
#     """,
#     """
#     CREATE TABLE IF NOT EXISTS certifications (
#         id SERIAL PRIMARY KEY,
#         document_id INT REFERENCES uploaded_documents(id) ON DELETE CASCADE,
#         certificate_names VARCHAR(255),
#         certificate_files BYTEA
#     )
#     """,
#     """
#     CREATE TABLE IF NOT EXISTS feedback (
#         id SERIAL PRIMARY KEY,
#         document_id INT REFERENCES uploaded_documents(id) ON DELETE SET NULL,
#         rating INT CHECK (rating BETWEEN 1 AND 5),
#         comments TEXT,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     )
#     """,
#     """
#     CREATE TABLE IF NOT EXISTS result (
#         result_id SERIAL PRIMARY KEY,
#         document_id INT REFERENCES uploaded_documents(id) ON DELETE CASCADE,
#         task_name VARCHAR(100),
#         task_status VARCHAR(20) DEFAULT 'Pending',
#         generated_result TEXT,
# print(git code upload code)
#         execution_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         completed BOOLEAN DEFAULT FALSE
#     )
#     """,
# ]
#
#
# def _conn_args(dbname):
#     return dict(
#         host=os.getenv("DB_HOST"),
#         database=dbname,
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         port=os.getenv("DB_PORT"),
#     )
#
#
# def ensure_database():
#     """Create the target database if it does not exist."""
#     target = os.getenv("DB_NAME")
#     try:
#         conn = psycopg2.connect(**_conn_args(target))
#         conn.close()
#         return  # already exists
#     except psycopg2.OperationalError as e:
#         if "does not exist" not in str(e):
#             raise
#
#     admin = psycopg2.connect(**_conn_args("postgres"))
#     admin.autocommit = True
#     try:
#         with admin.cursor() as cur:
#             cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(target)))
#         print(f"[init_db] Created database '{target}'")
#     finally:
#         admin.close()
#
#
# def ensure_tables():
#     conn = psycopg2.connect(**_conn_args(os.getenv("DB_NAME")))
#     try:
#         with conn.cursor() as cur:
#             for stmt in SCHEMA_STATEMENTS:
#                 cur.execute(stmt)
#         conn.commit()
#     finally:
#         conn.close()
#
#
# def init_db():
#     """Never crashes the API: prints a clear message if Postgres is unreachable."""
#     try:
#         ensure_database()
#         ensure_tables()
#         print("[init_db] Database ready: uploaded_documents, certifications, result, feedback, users")
#         return True
#     except Exception as e:
#         print(f"[init_db] WARNING: could not prepare the database -> {type(e).__name__}: {e}")
#         print("[init_db] Check that PostgreSQL is running and DB_* values in .env are correct.")
#         return False
#

# print(git code upload code)