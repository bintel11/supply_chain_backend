# app/services/placement.py
from app.db.models_inventory import Inventory, Warehouse

class Placement:
    """Simple greedy placement algorithm"""

    @staticmethod
    def place_item(items, warehouses):
        placement = {}
        for item in items:
            for wh in warehouses:
                if wh.capacity >= item.quantity:
                    placement[item.id] = wh.id
                    wh.capacity -= item.quantity
                    break
        return placement
