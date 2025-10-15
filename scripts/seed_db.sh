#!/usr/bin/env bash
# 🌱 Seed the test or local database with initial data

set -e

echo "🌿 Seeding database..."
python - <<'EOF'
from app.db.session import SessionLocal
from app.db.models_user import User
from app.db.seed_data import seed_initial_data

db = SessionLocal()
seed_initial_data(db)
print("✅ Database seeded successfully.")
EOF
