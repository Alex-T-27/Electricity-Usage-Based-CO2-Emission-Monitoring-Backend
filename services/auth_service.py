from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from db.models import User

# Load RSA keys from files
with open("private.pem", "r") as f:
    PRIVATE_KEY = f.read()

with open("public.pem", "r") as f:
    PUBLIC_KEY = f.read()

ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# This handles password hashing and verification
pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(password: str) -> str:
    return pwd_context.hash(password)
    # e.g. "mysecret" → "$2b$12$KIX..." (unreadable hash)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
    # checks if plain password matches the stored hash


def create_access_token(username: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": username,   # "sub" = subject — standard JWT field for who this token belongs to
        "exp": expire      # "exp" = expiry — JWT will be rejected after this time
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm=ALGORITHM)
    # Signs the token with the PRIVATE key


def decode_access_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")   # returns the username
    except JWTError:
        return None
    # Verifies using the PUBLIC key — raises JWTError if tampered or expired


def get_user(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def authenticate_user(db: Session, username: str, password: str) -> User | None:
    user = get_user(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

