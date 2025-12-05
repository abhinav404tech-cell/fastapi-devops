# app/services.py
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from . import repository
from .schemas import UserCreate

async def create_user_service(db: AsyncSession, payload: UserCreate):
    # example business rule: unique email
    existing = await repository.get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await repository.create_user(db, payload.username, payload.email)

async def get_user_service(db: AsyncSession, user_id: int):
    user = await repository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
