# app/services/inventory_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models_inventory import Inventory, Warehouse
from pydantic import BaseModel

class InventoryService:

    @staticmethod
    async def create_inventory(db: AsyncSession, item: BaseModel):
        inv = Inventory(name=item.name, quantity=item.quantity, warehouse_id=item.warehouse_id)
        db.add(inv)
        await db.commit()
        await db.refresh(inv)
        return inv

    @staticmethod
    async def get_all_inventory(db: AsyncSession):
        result = await db.execute(select(Inventory))
        return result.scalars().all()

    @staticmethod
    async def create_warehouse(db: AsyncSession, w: BaseModel):
        warehouse = Warehouse(name=w.name, location=w.location)
        db.add(warehouse)
        await db.commit()
        await db.refresh(warehouse)
        return warehouse

    @staticmethod
    async def get_all_warehouses(db: AsyncSession):
        result = await db.execute(select(Warehouse))
        return result.scalars().all()
