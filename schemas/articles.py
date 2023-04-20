from typing import Optional

from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    id: Optional[int] = Field(None)
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=100)

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True

        schema_extra = {
            "example": {
                "id": 1,
                "title": "Article 1",
                "description": "This is the first article",
            }
        }
