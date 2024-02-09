from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .dependencies import get_db, get_current_user
from .models import User, Contact
from .utils import hash_password, verify_password, create_access_token
from .routers import contacts, auth

# Завантаження змінних середовища
load_dotenv()

# Налаштування бази даних
DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Налаштування FastAPI
app = FastAPI()

# Конфігурація CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Створення таблиць у базі даних
Base.metadata.create_all(bind=engine)

# Підключення роутерів
app.include_router(contacts.router)
app.include_router(auth.router)
