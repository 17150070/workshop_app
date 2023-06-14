from pydantic import BaseModel, Field


class Shop(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=7)
    side: str
    price: float = Field(ge=0)     # ge - фильтер, означающий больше или равно, чем 0
    amount: float
