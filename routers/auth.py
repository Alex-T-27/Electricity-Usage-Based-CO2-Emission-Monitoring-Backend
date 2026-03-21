from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from db.database import get_db
from db.models import User
from services.auth_service import (
    hash_password,
    authenticate_user,
    create_access_token,
)

router = APIRouter()


class AuthRequest(BaseModel):
    username: str
    password: str


@router.post("/register")
def register(body: AuthRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == body.username).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Username already taken",
        )

    user = User(
        username=body.username,
        hashed_password=hash_password(body.password),  # hash before storing
    )

    db.add(user)
    db.commit()

    return {"message": "User registered successfully"}


@router.post("/login")
def login(body: AuthRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, body.username, body.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    token = create_access_token(user.username)

    return {
        "access_token": token,
        "token_type": "bearer",
    }
