from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os
print("database loading")
load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)
BASE=declarative_base()
SessionLocal=sessionmaker(
    bind=engine,
    autoflush= False,
    autocommit=False
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#checking the connection is made
# from sqlalchemy import text

# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT 1"))
#         print(result.scalar())
#         print(" Database Connected")
# except Exception as e:
#     print(f" Error: {e}")