
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import mysql.connector

#engineでデータベースと接続している
engine = create_engine(f'mysql+mysqlconnector://codeserver:rH8,KeGa@localhost/test')
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

session = scoped_session(
    # ORマッパーの設定。自動コミットと自動反映はオフにする
    SessionLocal
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()