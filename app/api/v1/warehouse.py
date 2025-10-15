# app/api/v1/warehouse.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.db.session import get_db
from app.services.inventory_service import InventoryService

router = APIRouter()

class WarehouseCreate(BaseModel):
    name: str
    location: str

@router.post("/")
async def create_warehouse(w: WarehouseCreate, db: AsyncSession = Depends(get_db)):
    warehouse = await InventoryService.create_warehouse(db, w)
    return warehouse

@router.get("/")
async def list_warehouses(db: AsyncSession = Depends(get_db)):
    warehouses = await InventoryService.get_all_warehouses(db)
    return warehouses
