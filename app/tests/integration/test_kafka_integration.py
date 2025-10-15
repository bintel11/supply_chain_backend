# app/tests/integration/test_kafka_integration.py
def test_kafka_mock():
    from app.integration.kafka_producer import send_kafka_event
    result = send_kafka_event("inventory_created", {"item": "Widget"})
    assert result is True
