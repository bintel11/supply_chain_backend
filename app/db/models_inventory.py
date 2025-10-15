# app/db/models_inventory.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String)
    capacity = Column(Integer, default=1000)

    inventory = relationship("Inventory", back_populates="warehouse")


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer, default=0)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"))

    warehouse = relationship("Warehouse", back_populates="inventory")
