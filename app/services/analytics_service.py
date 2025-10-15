# app/services/analytics_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models_order import Order
from app.db.models_inventory import Inventory

class AnalyticsService:

    @staticmethod
    async def get_kpis(db: AsyncSession):
        total_orders = await db.execute("SELECT COUNT(*) FROM orders")
        total_inventory = await db.execute("SELECT SUM(quantity) FROM inventory")
        return {"total_orders": total_orders.scalar(), "total_inventory": total_inventory.scalar()}
