from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from passlib.hash import sha256_crypt

from database.db import User, database
from helpers.jwt_fastapi import create_access_token
from schemas.users import UserLoginSchema

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(user: UserLoginSchema):
    query = User.select().where(User.c.username == user.username)
    user_db = await database.fetch_one(query)

    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    if not sha256_crypt.verify(user.password, user_db.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token = create_access_token(data={"sub": user_db.username})

    return {"access_token": access_token, "token_type": "bearer"}
