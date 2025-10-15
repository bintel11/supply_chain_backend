# app/tests/benchmark/test_query_performance.py
from app.db.session import SessionLocal
import time

def test_query_performance():
    db = SessionLocal()
    start = time.time()
    db.execute("SELECT 1")
    assert (time.time() - start) < 0.1
    db.close()
