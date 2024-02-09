from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Замініть на свої дані
DATABASE_URL = os.getenv("DATABASE_URL", DATABASE_URL)  # Опціонально: зчитуємо дані із змінної середовища, якщо вона встановлена

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Інші конфігураційні параметри можна додати за необхідності

def init_db():
    from .models import Base
    Base.metadata.create_all(bind=engine)
