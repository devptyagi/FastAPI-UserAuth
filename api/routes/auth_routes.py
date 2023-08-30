from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.service import user_service
from api.utils import password_util, jwt_util
from api.schemas.user import UserResponse, CreateUser, LoginResponse, LoginUser
from core.database import get_db

router = APIRouter()


@router.post("/signup", response_model=UserResponse)
def signup(user: CreateUser, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_service.create_user(db, user)


@router.post("/login", response_model=LoginResponse)
def login(credentials: LoginUser, db: Session = Depends(get_db)):
    db_user = user_service.get_user(db, credentials.email)

    if not db_user or not password_util.verify_password(credentials.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    access_token = jwt_util.create_token(data={"sub": db_user.email})
    user_response = UserResponse.model_validate(db_user)
    return LoginResponse(user=user_response, access_token=access_token)
