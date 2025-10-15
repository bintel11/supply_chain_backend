#!/usr/bin/env bash
# 🧪 Run unit, integration, and benchmark tests

set -e

echo "📦 Installing test dependencies..."
pip install -r requirements.txt > /dev/null

echo "🧹 Cleaning old test database..."
rm -f test.db || true

echo "🧪 Running pytest with coverage..."
pytest --maxfail=2 --disable-warnings --cov=app --cov-report=term-missing app/tests/

echo "✅ All tests completed successfully."
