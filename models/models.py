from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON

metadata = MetaData()

roles = Table(
    "roles",
    metadata, # прописываем, чтобы данные изменялись для миграций и учли, что создаем таблицу ролей
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),# datetime.utcnow - в зависимости от часового пояса указывается дата регистрации, то есть универсальный часовой пояс
    Column("role_id", Integer, ForeignKey("roles.id")),
)
