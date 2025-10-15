# app/api/v1/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, constr
from app.api.dependencies import get_db
from app.services.auth_service import AuthService
from app.db.models_user import User

router = APIRouter(tags=["Auth"])

# -------------------- Schemas --------------------
class RegisterRequest(BaseModel):
    username: constr(min_length=3, max_length=50)
    password: constr(min_length=6, max_length=72)  # bcrypt limit
    role: str = "viewer"

class LoginRequest(BaseModel):
    username: constr(min_length=3, max_length=50)
    password: constr(min_length=6, max_length=72)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# -------------------- Routes --------------------
@router.post("/register", response_model=RegisterRequest)
def register_user(req: RegisterRequest, db: Session = Depends(get_db)):
    """Register a new user."""
    existing = db.query(User).filter(User.username == req.username).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    user = AuthService.register_user(db, req.username, req.password, req.role)
    return RegisterRequest(username=user.username, password="********", role=user.role)

@router.post("/login", response_model=TokenResponse)
def login_user(req: LoginRequest, db: Session = Depends(get_db)):
    """Login user and return JWT token."""
    token = AuthService.authenticate_user(db, req.username, req.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return TokenResponse(access_token=token)
