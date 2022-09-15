
from pydantic import BaseModel


#BaseClassの作成
class ArticleBase(BaseModel):
    title: str
    content: str

class StudentBase(BaseModel):
    name: str
    mail: str
    passwd: str

#CreateClassの作成
class ArticleCreate(ArticleBase):
    is_display: bool

class StudentCreate(StudentBase):
    is_display: bool

class ArticleDisplay(ArticleBase):
    id: int
    class Config():
        orm_mode = True

class StudentDisplay(StudentBase):
    id: int

    class Config():
        orm_mode = True