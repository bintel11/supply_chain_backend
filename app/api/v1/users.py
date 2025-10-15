# app/api/v1/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.auth_service import AuthService
from app.api.dependencies import get_current_user

router = APIRouter()

@router.get("/me")
async def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.get("/")
async def list_users(db: AsyncSession = Depends(get_db)):
    users = await AuthService.get_all_users(db)
    return users
