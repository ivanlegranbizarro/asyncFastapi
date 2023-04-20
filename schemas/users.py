from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id: Optional[int] = Field(None)
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=3, max_length=500)

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True

        schema_extra = {
            "example": {
                "id": 1,
                "username": "user1",
                "email": "user1@user.com",
                "password": "password",
            }
        }


class UserOutputSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id": 1,
                "username": "user1",
                "email": "user1@user.com"
            }
        }


class UserLoginSchema(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "username": "user1",
                "password": "password",
            }
        }
