from sqlalchemy import Column, String
from core.database import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()), unique=True, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String, index=True)
    phone = Column(String)
