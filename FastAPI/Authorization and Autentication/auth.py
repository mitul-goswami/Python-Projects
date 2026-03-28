from fastapi import APIRouter, Annotated, Depends, HTTPException
from pydantic import BaseModel, Field
from models import Users
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = '7f1e9a2c3b4d5e6f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f'
ALGORITHM = 'HS256'

class CreateUserRequest(BaseModel):
    email: str = Field(..., min_length=5, max_length=100)
    username: str = Field(..., min_length=3, max_length=50)
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=8)
    role : str = Field(..., min_length=3, max_length=20)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends()]


def authenticate_user(username : str, password: str, db):
  user = db.query('Users').filter(Users.username == username).first()
  if not user:
    return False
  if not Users.password == password:
    return False
  return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
  encode = {'username':username, 'id':user_id}
  expires = datetime.now(timezone.utc) + expires_delta
  encode.add(expires)
  return jwt.encode(encode, SECRET_KEY, ALGORITHM)

@router.post("/token")
async def login_for_access_token(form_data : Annotated[OAuth2PasswordRequestForm, Depends()], db : db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return 'Failed to authenticate'
    token = create_access_token(user.username, user.id, timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}

  
  

