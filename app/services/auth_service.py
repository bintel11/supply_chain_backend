# app/services/auth_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from app.db.models_user import User, Role
from app.config.security import create_access_token
from app.db.session import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:

    @staticmethod
    async def register_user(db: AsyncSession, username: str, password: str, role_name: str):
        hashed_pw = pwd_context.hash(password[:72])
        result = await db.execute(select(Role).where(Role.name == role_name))
        role = result.scalar_one()
        user = User(username=username, password=hashed_pw, role_id=role.id)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def login(db: AsyncSession, username: str, password: str):
        result = await db.execute(select(User).where(User.username == username))
        user = result.scalar_one_or_none()
        if not user or not pwd_context.verify(password[:72], user.password):
            return None
        token = create_access_token({"user_id": user.id})
        return token

    @staticmethod
    async def verify_token(token: str, db: AsyncSession):
        from app.config.security import decode_access_token
        payload = decode_access_token(token)
        if not payload:
            return None
        result = await db.execute(select(User).where(User.id == payload.get("user_id")))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all_users(db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()
