from fastapi import FastAPI
import psycopg

from .database import router as db_router
from .router.users import router as users_router

app = FastAPI()
app.include_router(db_router)
app.include_router(users_router)



@app.get("/")
def root():
    return {"message": "Hello world"}

# @app.get("/users")
