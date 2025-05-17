from pydantic import BaseModel, EmailStr

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