from fastapi import APIRouter, HTTPException, status
from ..database import pool
from ..schemas import User, UserOutput, CreateUser, AdminUserOutput
from passlib.context import CryptContext
from typing import List

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#LOGIN 
#TODO: I will need to learn more about JWT so that I can save the JWT in the pydantic model
#TODO: Possibly use OAuth2 for protected route (not sure what that means just yet)
@router.post("/login", response_model=UserOutput)
def login():
    return {}

#REGISTER
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: CreateUser):
    CHECK_EMAIL = """
        SELECT 1 FROM users WHERE email = %s
    """
    
    #ORDER OF INPUT SHALL BE 1. Email 2. Password 3. First Name 4. Last Name
    REGISTER_USER = """
        INSERT INTO users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)
    """
    #HASH
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(CHECK_EMAIL, (user.email,))
            if cur.fetchone():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email: {user.email} already exists")
            cur.execute(REGISTER_USER, (user.email, user.password, user.first_name, user.last_name))
            conn.commit()
    return {"status": "user successfully created"}

#LOGOUT
@router.post("/logout")
def logout():
    return {}

#SHOULD ONLY BE ACCESSIBLE TO ADMINS
@router.get("/users", response_model=List[AdminUserOutput])
def get_users():
    SELECT_USERS = """
        SELECT user_id, first_name, last_name, email FROM users
    """
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(SELECT_USERS)
            rows = cur.fetchall()
            users = [
                {
                    "user_id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3]
                }
                for row in rows
            ]
    return users
