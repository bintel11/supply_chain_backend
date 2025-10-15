# app/api/router.py
from fastapi import APIRouter
from app.api.v1 import (
    auth,
    users,
    inventory,
    orders,
    warehouse,
    packages,
    tracking_ws,
    analytics,
    robotics
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(warehouse.router, prefix="/warehouses", tags=["warehouses"])
api_router.include_router(packages.router, prefix="/packages", tags=["packages"])
api_router.include_router(tracking_ws.router, prefix="/tracking", tags=["tracking"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
api_router.include_router(robotics.router, prefix="/robotics", tags=["robotics"])
