# print(git code upload code)
# """
# Authentication: register / login / forgot-password + a middleware that
# requires a valid token for every /api/* route except the auth routes
# and /api/health. The existing endpoints themselves are unchanged.
# """
# import hashlib
# import hmac
# import os
# import re
# import secrets
# from datetime import datetime, timedelta, timezone
#
# import jwt
# from fastapi import APIRouter, Form, HTTPException, Request
# from fastapi.responses import JSONResponse
#
# from db import get_connection
#
# router = APIRouter(prefix="/api/auth", tags=["auth"])
#
# TOKEN_HOURS = 12
# PUBLIC_PATHS = {"/api/health"}
# _fallback_secret = secrets.token_hex(32)
#
#
# # ---------------------------------------------------------------
# # helpers
# # ---------------------------------------------------------------
# def _secret():
#     key = os.getenv("SECRET_KEY")
#     if not key:
#         print("[auth] WARNING: SECRET_KEY missing in .env - using a temporary key")
#         return _fallback_secret
#     return key
#
#
# def _algorithm():
#     return os.getenv("ALGORITHM") or "HS256"
#
#
# def hash_password(password: str) -> str:
#     salt = secrets.token_bytes(16)
#     iters = 200_000
#     digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iters)
#     return f"pbkdf2${iters}${salt.hex()}${digest.hex()}"
#
#
# def verify_password(password: str, stored: str) -> bool:
#     try:
#         _, iters, salt_hex, hash_hex = stored.split("$")
#         digest = hashlib.pbkdf2_hmac(
#             "sha256", password.encode(), bytes.fromhex(salt_hex), int(iters)
#         )
#         return hmac.compare_digest(digest.hex(), hash_hex)
#     except Exception:
#         return False
#
#
# def create_token(username: str) -> str:
#     payload = {
#         "sub": username,
#         "exp": datetime.now(timezone.utc) + timedelta(hours=TOKEN_HOURS),
#     }
#     return jwt.encode(payload, _secret(), algorithm=_algorithm())
#
#
# def decode_token(token: str) -> str:
#     data = jwt.decode(token, _secret(), algorithms=[_algorithm()])
#     return data["sub"]
#
#
# def _db_one(query, params):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute(query, params)
#         return cur.fetchone()
#     finally:
#         cur.close()
#         conn.close()
#
#
# # ---------------------------------------------------------------
# # middleware: protect every /api/* route except public ones
# # ---------------------------------------------------------------
# async def auth_middleware(request: Request, call_next):
#     path = request.url.path
#     if (
#         request.method == "OPTIONS"
#         or not path.startswith("/api/")
#         or path in PUBLIC_PATHS
#         or path.startswith("/api/auth/login")
#         or path.startswith("/api/auth/register")
#         or path.startswith("/api/auth/reset-password")
#     ):
#         return await call_next(request)
#
#     header = request.headers.get("Authorization", "")
#     token = header[7:] if header.lower().startswith("bearer ") else ""
#     try:
#         request.state.user = decode_token(token)
#     except Exception:
#         return JSONResponse(
#             status_code=401,
#             content={"detail": "Please log in to continue."},
#             headers={"Access-Control-Allow-Origin": "*"},
#         )
#     return await call_next(request)
#
#
# # ---------------------------------------------------------------
# # routes
# # ---------------------------------------------------------------
# @router.post("/register")
# def register(
#     username: str = Form(...),
#     full_name: str = Form(""),
#     email: str = Form(...),
#     mobile: str = Form(""),
#     password: str = Form(...),
# ):
#     username = username.strip().lower()
#     full_name = full_name.strip()
#     email = email.strip().lower()
#     mobile = mobile.strip()
# print(git code upload code)
#
#     if not re.fullmatch(r"[a-z0-9_.-]{3,30}", username):
#         raise HTTPException(400, "Username must be 3-30 characters (letters, numbers, . _ -).")
#     if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
#         raise HTTPException(400, "Please enter a valid email address.")
#     if len(full_name) > 100:
#         raise HTTPException(400, "Full name must be 100 characters or fewer.")
#     if mobile and not re.fullmatch(r"[+()\d\s.-]{7,25}", mobile):
#         raise HTTPException(400, "Please enter a valid mobile number.")
#     if len(password) < 6:
#         raise HTTPException(400, "Password must be at least 6 characters.")
#
#     if _db_one("SELECT 1 FROM users WHERE username = %s", (username,)):
#         raise HTTPException(409, "That username is already taken.")
#
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute(
#             """
#             INSERT INTO users (username, full_name, email, mobile, password_hash)
#             VALUES (%s, %s, %s, %s, %s)
#             """,
#             (username, full_name or None, email, mobile or None, hash_password(password)),
#         )
#         conn.commit()
#     except Exception:
#         conn.rollback()
#         raise
#     finally:
#         cur.close()
#         conn.close()
#
#     return {"status": "created", "username": username}
#
#
# @router.post("/login")
# def login(username: str = Form(...), password: str = Form(...)):
#     username = username.strip().lower()
#     row = _db_one("SELECT id, password_hash FROM users WHERE username = %s", (username,))
#
#     if not row or not verify_password(password, row[1]):
#         raise HTTPException(401, "Invalid username or password.")
#
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute(
#             """
#             UPDATE users
#             SET login_count = login_count + 1, last_login_at = CURRENT_TIMESTAMP
#             WHERE id = %s
#             """,
#             (row[0],),
#         )
#         conn.commit()
#     except Exception:
#         conn.rollback()
#         raise
#     finally:
#         cur.close()
#         conn.close()
#
#     return {"token": create_token(username), "username": username}
#
#
# @router.post("/reset-password")
# def reset_password(
#     username: str = Form(...),
#     email: str = Form(...),
#     new_password: str = Form(...),
# ):
#     username = username.strip().lower()
#     email = email.strip().lower()
#
#     if len(new_password) < 6:
#         raise HTTPException(400, "Password must be at least 6 characters.")
#
#     row = _db_one(
#         "SELECT id FROM users WHERE username = %s AND email = %s", (username, email)
#     )
#     if not row:
#         raise HTTPException(404, "No account matches that username and email.")
#
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute(
#             "UPDATE users SET password_hash = %s WHERE id = %s",
#             (hash_password(new_password), row[0]),
#         )
#         conn.commit()
#     except Exception:
#         conn.rollback()
#         raise
#     finally:
#         cur.close()
#         conn.close()
#
#     return {"status": "password_updated"}
#
#
# @router.get("/me")
# def me(request: Request):
#     username = getattr(request.state, "user", None)
#     row = _db_one(
#         """
#         SELECT username, full_name, email, mobile, login_count, last_login_at, created_at
#         FROM users WHERE username = %s
#         """,
#         (username,),
#     )
#     if not row:
#         raise HTTPException(404, "User profile was not found.")
#
#     return {
#         "username": row[0],
#         "full_name": row[1],
#         "email": row[2],
#         "mobile": row[3],
#         "login_count": row[4],
#         "last_login_at": row[5],
#         "created_at": row[6],
#     }
#

# print(git code upload code)