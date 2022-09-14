from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(String(100))
    is_display = Column(Boolean, default=False)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    mail = Column(String(100))
    #パスワードは64文字までらしい
    passwd = Column(String(64))

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    #教員の担当科目
    tantou = Column(String(50))
    mail = Column(String(100))
    passwd = Column(String(64))

class Kougi(Base):
    __tablename__ = 'kougis'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    summary = Column(String(255))
    #これとteacherのidを結びつける必要がある