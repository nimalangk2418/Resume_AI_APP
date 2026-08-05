"""
api/auth.py

Recruiter Authentication API
JWT Authentication
"""

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from jose import JWTError, jwt

from passlib.context import CryptContext

from PythonFiles_RAG.backend.database.connection import get_db
from PythonFiles_RAG.backend.database.models import Recruiter

from PythonFiles_RAG.backend.utils.config import settings
from PythonFiles_RAG.backend.utils.logger import logger


# ==========================================================
# Router
# ==========================================================

router = APIRouter()


# ==========================================================
# Password Encryption
# ==========================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# ==========================================================
# Password Functions
# ==========================================================

def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ==========================================================
# JWT Token
# ==========================================================

def create_access_token(data: dict):

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = data.copy()

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


# ==========================================================
# Register Recruiter
# ==========================================================

@router.post("/register")

def register(

    full_name: str,

    email: str,

    password: str,

    db: Session = Depends(get_db)

):

    recruiter = db.query(Recruiter).filter(
        Recruiter.email == email
    ).first()

    if recruiter:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = Recruiter(

        full_name=full_name,

        email=email,

        password=hash_password(password)

    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    logger.info(f"Recruiter Registered : {email}")

    return {

        "message": "Registration Successful"

    }


# ==========================================================
# Login
# ==========================================================

@router.post("/login")

def login(

    email: str,

    password: str,

    db: Session = Depends(get_db)

):

    recruiter = db.query(Recruiter).filter(
        Recruiter.email == email
    ).first()

    if recruiter is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid Email"

        )

    if not verify_password(
        password,
        recruiter.password
    ):

        raise HTTPException(

            status_code=401,

            detail="Invalid Password"

        )

    token = create_access_token(

        {

            "sub": recruiter.email,

            "id": recruiter.recruiter_id

        }

    )

    logger.info(f"Recruiter Login : {email}")

    return {

        "access_token": token,

        "token_type": "bearer"

    }


# ==========================================================
# Current User
# ==========================================================

@router.get("/me")

def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    credentials_exception = HTTPException(

        status_code=status.HTTP_401_UNAUTHORIZED,

        detail="Invalid Token"

    )

    try:

        payload = jwt.decode(

            token,

            settings.SECRET_KEY,

            algorithms=[settings.ALGORITHM]

        )

        email = payload.get("sub")

    except JWTError:

        raise credentials_exception

    recruiter = db.query(Recruiter).filter(

        Recruiter.email == email

    ).first()

    if recruiter is None:

        raise credentials_exception

    return {

        "Recruiter ID": recruiter.recruiter_id,

        "Name": recruiter.full_name,

        "Email": recruiter.email,

        "Role": recruiter.role

    }