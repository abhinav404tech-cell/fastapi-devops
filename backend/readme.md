# fastapi-3tier (single API)

Run:
1. Set DATABASE_URL in .env (or use default sqlite aiosqlite).
2. Create venv, install:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
3. Run:
   uvicorn app.main:app --reload

Endpoints:
POST /users        -> create user
GET  /users/{id}   -> get user

Notes:
- This is async SQLAlchemy. For production use Alembic for migrations and better config management.
