# app/tests/automation/test_performance_metrics.py
def test_metrics_decorator():
    from app.utils.metrics import timing

    @timing
    def slow_func():
        sum([x for x in range(100000)])
        return True

    assert slow_func() is True
