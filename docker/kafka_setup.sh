#!/usr/bin/env bash
# 🧩 Create Kafka topics for supply chain system

set -e

KAFKA_BROKER="localhost:9092"
TOPICS=("inventory_events" "order_updates" "robot_status" "analytics_stream")

echo "📡 Creating Kafka topics..."
for topic in "${TOPICS[@]}"; do
  docker exec -it supply_kafka kafka-topics.sh --create \
    --if-not-exists \
    --bootstrap-server "$KAFKA_BROKER" \
    --replication-factor 1 \
    --partitions 3 \
    --topic "$topic" || true
done

echo "✅ Kafka topics ready."
