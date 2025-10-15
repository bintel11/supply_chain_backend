#!/usr/bin/env bash
# 🚀 Start FastAPI development server

set -e  # Exit on error

echo "🔧 Activating virtual environment..."
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "⚠️  No virtual environment found. Run 'python -m venv venv && source venv/bin/activate'"
    exit 1
fi

echo "✅ Environment activated."

echo "🧠 Running database migrations..."
alembic upgrade head || echo "⚠️  Migration skipped (check Alembic setup)"

echo "🏗️ Starting FastAPI app on port 8000..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
