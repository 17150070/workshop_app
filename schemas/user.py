from typing import List, Optional
from pydantic import BaseModel

from schemas.degree import Degree

import uuid

from fastapi_users import schemas
#
#
# class User(BaseModel):
#     id:int
#     role: str
#     name: str
#     degree: Optional[List[Degree]] = []



class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    email: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
