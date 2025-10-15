# app/services/tracking_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models_tracking import Package
from fastapi import WebSocket

class TrackingService:

    @staticmethod
    async def create_package(db: AsyncSession, order_id: int):
        package = Package(order_id=order_id, status="created")
        db.add(package)
        await db.commit()
        await db.refresh(package)
        return package

    @staticmethod
    async def get_all_packages(db: AsyncSession):
        result = await db.execute(select(Package))
        return result.scalars().all()

    @staticmethod
    async def handle_ws_message(ws: WebSocket, message: str):
        await ws.send_text(f"Received: {message}")
