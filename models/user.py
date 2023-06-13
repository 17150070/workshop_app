from typing import List, Optional
from pydantic import BaseModel

from models.degree import Degree


class User(BaseModel):
    id:int
    role: str
    name: str
    degree: Optional[List[Degree]] = []
