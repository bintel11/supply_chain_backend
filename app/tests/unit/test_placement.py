# app/tests/unit/test_placement.py
from app.services.placement import greedy_placement

def test_greedy_placement():
    items = [10, 20, 30]
    capacity = 50
    result = greedy_placement(items, capacity)
    assert sum(result) <= capacity
