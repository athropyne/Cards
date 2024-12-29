import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, DateTime

metadata = MetaData()

users = Table(
    "accounts",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String, unique=True, nullable=False),
    Column("password", String, nullable=False)
)
