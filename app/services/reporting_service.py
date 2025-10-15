# app/services/reporting_service.py
import csv
from app.db.models_order import Order

class ReportingService:

    @staticmethod
    def export_orders_csv(orders, filepath="orders.csv"):
        with open(filepath, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Order ID", "User ID"])
            for order in orders:
                writer.writerow([order.id, order.user_id])
        return filepath
