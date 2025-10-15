# app/api/v1/analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.analytics_service import AnalyticsService

router = APIRouter()

@router.get("/kpis")
async def get_kpis(db: AsyncSession = Depends(get_db)):
    return await AnalyticsService.get_kpis(db)
