# app/api/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import UserCreate, UserRead
from ..db import get_db
from ..services import create_user_service, get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserRead, status_code=201)
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user_service(db, payload)

@router.get("/", response_model=UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_user_service(db, user_id)

@router.get("/hello")
async def read_user():
    return {"message":"hello"}
