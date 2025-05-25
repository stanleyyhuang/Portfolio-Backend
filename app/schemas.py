from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    password: str
    user_id: int

class CreateUser(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str

class UserOutput(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

class AdminUserOutput(UserOutput):
    user_id: int

class loginUser(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None
    