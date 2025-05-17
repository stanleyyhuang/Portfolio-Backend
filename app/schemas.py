from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    password: str
    user_id: int

class CreateUser(BaseModel):
    email: EmailStr
    password: str

class UserOutput(BaseModel):
    email: EmailStr
    