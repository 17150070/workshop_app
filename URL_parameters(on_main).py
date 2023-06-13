from fastapi import FastAPI

app = FastAPI(
    title="Workshop App"
)

shop = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 133, "amount": 2.12},
]

@app.get("/shops/")
def get_shops(limit: int = 1, offset: int = 0): # offset - страница(сдвиг), limit - количество записей на странице
    return shop[offset:][:limit]


users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "admin", "name": "Rail"},
    {"id": 3, "role": "admin", "name": "Skyline"},
]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}
