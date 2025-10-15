# app/api/v1/orders.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List
from app.db.session import get_db
from app.services.order_service import OrderService

router = APIRouter()

class OrderItemCreate(BaseModel):
    inventory_id: int
    quantity: int

class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItemCreate]

@router.post("/")
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    new_order = await OrderService.create_order(db, order)
    return new_order

@router.get("/")
async def list_orders(db: AsyncSession = Depends(get_db)):
    orders = await OrderService.get_all_orders(db)
    return orders
