from fastapi import APIRouter,Depends
from app.dependencies import get_current_user
from app.services.auth_service import register_user,User_Login,refresh_token
from app.schemas.user import UserCreate,UserLogin,UserResponse,RefreshTokenRequest
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User

router=APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register",response_model=UserResponse)
def register(data:UserCreate,db:Session=Depends(get_db)):
    return register_user(db,data.email,data.password)

@router.post("/login")
def login(data:UserLogin,db:Session=Depends(get_db)):
    return User_Login(db,data.email,data.password)

@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)):
    return current_user
