# app/integration/kafka_consumer.py
from aiokafka import AIOKafkaConsumer
import asyncio
from app.config.settings import KAFKA_BOOTSTRAP_SERVERS

async def consume(topic: str, group_id: str):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=group_id,
        auto_offset_reset="earliest"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"Consumed: {msg.topic}:{msg.partition}:{msg.offset}: key={msg.key} value={msg.value}")
    finally:
        await consumer.stop()
