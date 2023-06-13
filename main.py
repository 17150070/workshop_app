from typing import List

from fastapi import FastAPI

from models.shop import Shop
from models.user import User

app = FastAPI(
    title="Workshop App"
)

users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "admin", "name": "Rail"},
    {"id": 3, "role": "admin", "name": "Skyline"},
    {"id": 4, "role": "admin", "name": "Skyline", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int): # указываем типизацию
    return [
        user for user in users # Проходимся по пользователям
        if user.get("id") == user_id # сравниваем данные из json с path-параметром
    ]

shop = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 133, "amount": 2.12},
]


@app.post("/shops")
def add_trades(shops: List[Shop]):
    shop.extend(shops) # extend - добавить
    return {"status": 200, "data": shop}
