from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

DATABASE_URL = "sqlite:///./fastapi.db"

engine = create_engine(DATABASE_URL)

metadata = MetaData()


Article = Table(
    "articles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50), nullable=False, unique=True),
    Column("description", String(100), nullable=False),
)

User = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False, unique=True),
    Column("email", String(50), nullable=False, unique=True),
    Column("password", String(500), nullable=False),
)


database = Database(DATABASE_URL)
