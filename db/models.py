from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(String(100))
    is_display = Column(Boolean, default=False)