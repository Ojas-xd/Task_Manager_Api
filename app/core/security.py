from app.core.config import settings
from jose import jwt,JWTError
from fastapi import HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta,timezone,datetime
ALGORITHM="HS256"
SECRET_KEY = settings.SECRET_KEY
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = settings.REFRESH_TOKEN_EXPIRE_DAYS
ALGORITHM="HS256"

#Password hashing Logic and Functions
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(password:str)->str:
    return pwd_context.hash(password)
def verify_password(plain_password:str,hashed_password:str)->str:
    return pwd_context.verify(plain_password,hashed_password)

#Token creation and verify
oauth2scheme=OAuth2PasswordBearer(tokenUrl="/login")
def create_access_token(Data:dict):
    to_encode=Data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire,"type":"access"})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
def create_refresh_token(Data:dict):
    to_encode=Data.copy()
    expire=datetime.now(timezone.utc)+timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp":expire,"type":"refresh"})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
def decode_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    