from datetime import datetime
from enum import Enum

from pydantic import BaseModel


# Валидация данных
class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


