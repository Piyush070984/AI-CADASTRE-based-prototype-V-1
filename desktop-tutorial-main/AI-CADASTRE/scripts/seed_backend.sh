#!/usr/bin/env sh
set -e
cd "$(dirname "$0")/../backend"
python - <<'PY'
from app.db.init_db import init_db, seed_db
from app.db.session import SessionLocal
init_db()
with SessionLocal() as db:
    seed_db(db)
print('Seed complete')
PY
