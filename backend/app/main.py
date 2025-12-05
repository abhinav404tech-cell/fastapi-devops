# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import engine, Base, DATABASE_URL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# import routers (do this after creating app)
from .api import users  # your router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    logger.info("LIFESPAN startup - DB URL: %s", DATABASE_URL)
    # ensure models are imported so Base.metadata knows them
    import app.models  # or: from . import models
    # create tables (async SQLAlchemy)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("tables created / checked")
    try:
        yield
    finally:
        # shutdown logic (if any)
        logger.info("LIFESPAN shutdown")

app = FastAPI(title="3-tier FastAPI - single API", lifespan=lifespan)

app.include_router(users.router)
