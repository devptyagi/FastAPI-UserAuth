from sqlalchemy.orm import Session
from api.schemas.user import CreateUser
from api.models.user import User
from api.utils import password_util


def get_user(db: Session, user_email: str):
    return db.query(User).filter_by(email=user_email).one_or_none()


def create_user(db: Session, user: CreateUser):
    hashed_password = password_util.generate_password_hash(user.password)
    db_user = User(email=user.email, password=hashed_password, full_name=user.full_name, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
