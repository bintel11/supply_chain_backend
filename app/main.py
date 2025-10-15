from fastapi import FastAPI
from app.api.v1 import auth, inventory, orders  # import your routers
from app.db.database import Base, engine

# Create tables if not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Warehouse Management System")

# Include existing auth router
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

# Include inventory router
app.include_router(inventory.router, prefix="/api/v1/inventory", tags=["Inventory"])

# Include orders router
app.include_router(orders.router, prefix="/api/v1/orders", tags=["Orders"])

# Health check
@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}
