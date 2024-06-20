from db import engine
from sqlmodel import SQLModel, Session
from sqlalchemy.engine import reflection
import models


def init_db():
    SQLModel.metadata.create_all(engine)
    print("Database initialized successfully")