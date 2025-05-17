from fastapi import FastAPI
import psycopg
from psycopg_pool import ConnectionPool
import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
USER = os.environ.get("POSTGRES_USER")
DATABASE = os.environ.get("POSTGRES_DATABASE")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")

# Connect to database
pool = ConnectionPool(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world"}

# @app.get("/users")
