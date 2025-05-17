from fastapi import APIRouter, status
from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
USER = os.environ.get("POSTGRES_USER")
DATABASE = os.environ.get("POSTGRES_DATABASE")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
# Connect to database
pool = ConnectionPool(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
router = APIRouter()

@router.get("/initialize", status_code=status.HTTP_201_CREATED)
def initialize_db():
    CREATE_USERS = """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT now()
        );
        """
    CREATE_BLOGS = """
        CREATE TABLE IF NOT EXISTS blogs (
            blog_id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            owner_id INT REFERENCES users(user_id),
            created_at TIMESTAMP DEFAULT now()
        );
        """
    CREATE_COMMENTS = """
        CREATE TABLE IF NOT EXISTS comments (
            comment_id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            owner_id INT NOT NULL REFERENCES users(user_id),
            blog_id INT NOT NULL REFERENCES blogs(blog_id),
            created_at TIMESTAMP DEFAULT now()
        );
        """
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_USERS)
            cur.execute(CREATE_BLOGS)
            cur.execute(CREATE_COMMENTS)
            conn.commit()
    return {"status": "Tables created"}

