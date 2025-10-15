#!/usr/bin/env bash
# 🚀 Deploy the app via Docker Compose or CI/CD pipeline

set -e

echo "🏗️ Building Docker image..."
docker-compose build

echo "📦 Starting containers..."
docker-compose up -d

echo "🧠 Applying migrations..."
docker-compose exec backend alembic upgrade head

echo "✅ Deployment successful! Access the app at http://localhost:8000"
