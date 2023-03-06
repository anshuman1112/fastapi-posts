from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings


#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

#FOR LOCAL NON DOCKER
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db_username}:{settings.db_pwd}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"

#FOR DOCKER
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@postgres/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# #
# # DB CONNECTION
# #
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', password='postgres', user='postgres', database = 'fastapi', cursor_factory = RealDictCursor)
        
#         #Uncomment for Docker
#         #conn = psycopg2.connect(host = 'postgres', password='postgres', user='postgres', database = 'fastapi', cursor_factory = RealDictCursor)
        
#         cursor = conn.cursor()
#         print("DB Connection successful")
#         break
#     except Exception as e:
#         print(f"DB connection failed with error, {e}")
#         time.sleep(2)