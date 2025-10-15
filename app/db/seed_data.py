# app/db/seed_data.py
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import async_session
from app.db.models_user import Role, User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def seed_roles():
    async with async_session() as db:
        roles = ["admin", "manager", "worker"]
        for r in roles:
            role = Role(name=r)
            db.add(role)
        await db.commit()

async def seed_users():
    async with async_session() as db:
        result = await db.execute("SELECT id FROM roles WHERE name='admin'")
        admin_role_id = result.scalar_one()
        user = User(username="admin", password=pwd_context.hash("admin123"[:72]), role_id=admin_role_id)
        db.add(user)
        await db.commit()

async def run_seed():
    await seed_roles()
    await seed_users()

if __name__ == "__main__":
    asyncio.run(run_seed())
