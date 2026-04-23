from fastapi import HTTPException
from app.models.user import User
from app.core.security import create_access_token,create_refresh_token,verify_password,decode_token
from app.core.security import hash_password

def register_user(db,email,password):
    q=db.query(User).filter(User.email==email).first()
    if q:
        raise HTTPException(status_code=404,detail="User Already Exists")
    ha=hash_password(password)
    new_user=User(email=email,hashed_password=ha)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def User_Login(db,email,password):
    q=db.query(User).filter(User.email==email).first()
    if not q:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    ver=verify_password(password,q.hashed_password)
    if not ver:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    access_token=create_access_token({"sub":str(q.id)})
    refresh_token=create_refresh_token({"sub":str(q.id)})
    return{
        "access_token":access_token,
        "refresh_token":refresh_token,
        "token_type":"bearer"
    }

def refresh_token(refreshtoken:str):
    payload=decode_token(refreshtoken)
    if payload is None:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    if payload.get("type")!="refresh":
        raise HTTPException(status_code=401,detail="Invalid credentials")
    
    user_id=payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    
    access_token=create_access_token({"sub":user_id})
    return{
        "access_token":access_token,
        "token_type":"bearer"
    }


