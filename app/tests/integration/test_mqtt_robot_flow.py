# app/tests/integration/test_mqtt_robot_flow.py
def test_mqtt_connection():
    from app.integration.mqtt_adapter import connect_mqtt
    client = connect_mqtt()
    assert client is not None
