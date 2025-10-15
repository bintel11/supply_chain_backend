# app/config/constants.py
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    WORKER = "worker"

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class InventoryStatus(str, Enum):
    IN_STOCK = "in_stock"
    RESERVED = "reserved"
    OUT_OF_STOCK = "out_of_stock"
