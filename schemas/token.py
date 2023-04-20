from typing import Union

from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    username: Union[str, None] = Field(None)
