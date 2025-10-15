# app/integration/kafka_producer.py
from aiokafka import AIOKafkaProducer
import asyncio
from app.config.settings import KAFKA_BOOTSTRAP_SERVERS

producer: AIOKafkaProducer = None

async def init_producer():
    global producer
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()

async def send_message(topic: str, value: str):
    if producer is None:
        await init_producer()
    await producer.send_and_wait(topic, value.encode("utf-8"))

async def shutdown_producer():
    if producer:
        await producer.stop()
