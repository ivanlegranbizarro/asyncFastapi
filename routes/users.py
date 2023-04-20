from typing import List

from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from database.db import User, database
from schemas.users import UserSchema, UserOutputSchema
from passlib.hash import sha256_crypt

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=List[UserOutputSchema], status_code=status.HTTP_200_OK)
async def get_all_users():
    query = User.select()
    return await database.fetch_all(query)


@router.get("/{user_id}", response_model=UserOutputSchema, status_code=status.HTTP_200_OK)
async def get_user(user_id: int):
    query = User.select().where(User.c.id == user_id)
    user = await database.fetch_one(query)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserOutputSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserSchema):
    try:
        query = User.insert().values(
            username=user.username,
            email=user.email,
            password=sha256_crypt.hash(user.password)
        )
        last_record_id = await database.execute(query)
        return {**user.dict(), "id": last_record_id}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
