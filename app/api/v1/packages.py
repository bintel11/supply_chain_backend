# app/api/v1/packages.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.db.session import get_db
from app.services.tracking_service import TrackingService

router = APIRouter()

class PackageCreate(BaseModel):
    order_id: int

@router.post("/")
async def create_package(pkg: PackageCreate, db: AsyncSession = Depends(get_db)):
    package = await TrackingService.create_package(db, pkg.order_id)
    return package

@router.get("/")
async def list_packages(db: AsyncSession = Depends(get_db)):
    packages = await TrackingService.get_all_packages(db)
    return packages
