# app/tests/benchmark/test_placement_benchmark.py
import time
from app.services.placement_optimizer import simulated_annealing

def test_placement_benchmark():
    items = [10, 20, 30, 40, 50]
    start = time.time()
    simulated_annealing(items, capacity=100)
    duration = time.time() - start
    assert duration < 2.0
