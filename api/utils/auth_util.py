from typing import Optional

from fastapi import HTTPException, Header, Depends, status
from sqlalchemy.orm import Session

from api.utils import jwt_util
from api.service import user_service
from core.database import get_db
from api.models.user import User


def get_current_user(auth_header: Optional[str] = Header(None, alias="Authorization"), db: Session = Depends(get_db)) -> User:
    if auth_header is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No token provided")

    scheme, _, token = auth_header.partition(' ')

    if scheme.lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization scheme")

    if not token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No token provided")

    try:
        payload = jwt_util.decode_token(token)
        email = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")

        db_user = user_service.get_user(db, email)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
