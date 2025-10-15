# app/api/v1/inventory.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.db.session import get_db
from app.services.inventory_service import InventoryService

router = APIRouter()

class InventoryCreate(BaseModel):
    name: str
    quantity: int
    warehouse_id: int

@router.post("/")
async def create_inventory(item: InventoryCreate, db: AsyncSession = Depends(get_db)):
    inv = await InventoryService.create_inventory(db, item)
    return inv

@router.get("/")
async def list_inventory(db: AsyncSession = Depends(get_db)):
    items = await InventoryService.get_all_inventory(db)
    return items
