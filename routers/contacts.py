from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db, get_current_user
from ..models import Contact
from pydantic import BaseModel

router = APIRouter()

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_data: str = None

@router.post("/contacts/")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # ваша реалізація ендпоінта
    pass

@router.get("/contacts/")
def read_contacts(q: str = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # ваша реалізація ендпоінта
    pass


