from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    email: str
    full_name: str
    phone: str


class CreateUser(UserBase):
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class UserResponse(UserBase):
    id: UUID4

    class Config:
        from_attributes = True


class LoginResponse(BaseModel):
    user: UserResponse
    access_token: str

    class Config:
        from_attributes = True
