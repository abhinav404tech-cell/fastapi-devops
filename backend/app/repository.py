# app/repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from .models import User

async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    q = await db.execute(select(User).where(User.id == user_id))
    return q.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    q = await db.execute(select(User).where(User.email == email))
    return q.scalars().first()

async def create_user(db: AsyncSession, username: str, email: str) -> User:
    user = User(username=username, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
