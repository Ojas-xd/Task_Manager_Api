from app.database import get_db
from app.core.security import oauth2scheme,decode_token
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.user import User
from fastapi import HTTPException


def get_current_user(token:str=Depends(oauth2scheme),db:Session=Depends(get_db)):
    payload=decode_token(token)
    if payload is None:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    user_id=payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    d=db.query(User).filter(User.id==int(user_id)).first()
    if not d:
        raise HTTPException(status_code=404,detail="Invalid")
    return d
    