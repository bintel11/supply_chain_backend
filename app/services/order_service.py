# app/services/order_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models_order import Order, OrderItem
from app.api.v1.orders import OrderCreate

class OrderService:

    @staticmethod
    async def create_order(db: AsyncSession, order: OrderCreate):
        new_order = Order(user_id=order.user_id)
        db.add(new_order)
        await db.flush()  # to get order.id
        for item in order.items:
            db.add(OrderItem(order_id=new_order.id, inventory_id=item.inventory_id, quantity=item.quantity))
        await db.commit()
        await db.refresh(new_order)
        return new_order

    @staticmethod
    async def get_all_orders(db: AsyncSession):
        result = await db.execute(select(Order))
        return result.scalars().all()
