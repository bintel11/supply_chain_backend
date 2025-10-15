# app/integration/mqtt_adapter.py
from asyncio_mqtt import Client
import asyncio
from app.config.settings import MQTT_BROKER_HOST, MQTT_BROKER_PORT

async def publish(topic: str, payload: str):
    async with Client(MQTT_BROKER_HOST, MQTT_BROKER_PORT) as client:
        await client.publish(topic, payload.encode())

async def subscribe(topic: str, callback):
    async with Client(MQTT_BROKER_HOST, MQTT_BROKER_PORT) as client:
        async with client.unfiltered_messages() as messages:
            await client.subscribe(topic)
            async for msg in messages:
                await callback(msg.topic, msg.payload.decode())
