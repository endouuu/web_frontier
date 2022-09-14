from sqlalchemy.orm.session import Session
from schemas import ArticleBase, ArticleCreate
from db.models import Article

#エンドポイント@get作る必要がある
#schema


# 新規登録
def create_article(db: Session, request: ArticleBase):
    new_article = Article(
        title = request.title,
        content = request.content,
        is_display = request.is_display
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

# 全ての登録情報を取得
#articleについて
def get_articles_all(db: Session):
    return db.query(Article).filter(Article.is_display == True).all()

def get_students_all(db: Session):
    return db.query(Student).filter(Student.is_display == True).all()

def get_teacher_all(db: Session):
    return db.query(Teacher).filter(Teacher.is_display == True).all()

def get_Kougi_all(db: Session):
    return db.query(Kougi).filter(Kougi.is_display == True).all()

# 登録内容情報取得
def get_article(db: Session, id: int):
    return db.query(Article).filter(Article.id == id).first()

def get_student(db: Session, id: int):
    return db.query(Student).filter(Student.id == id).first()

def get_teacher(db: Session, id: int):
    return db.query(Teacher).filter(Teacher.id == id).first()

def get_kougi(db: Session, id: int):
    return db.query(Kougi).filter(Kougi.id == id).first()

# 登録内容更新
def update_article(db: Session, id: int, request: ArticleCreate):
    article = db.query(Article).filter(Article.id == id)
    article.update({
        Article.title: request.title,
        Article.content: request.content,
        Article.is_display: request.is_display
    })
    db.commit()
    return {'message': 'success'}

def update_student(db: Session, id: int, request: ArticleCreate):
    student = db.query(Student).filter(Student.id == id)
    student.update({
        Student.name: request.name,
        Student.mail: request.mail,
        Student.passwd: request.passwd
    })
    db.commit()
    return {'message': '学生データの更新をしました'}

def update_teacher(db: Session, id: int, request: ArticleCreate):
    teacher = db.query(Teacher).filter(Teacher.id == id)
    teacher.update({
        Teacher.name: request.name,
        Teacher.tantou: request.tantou,
        Teacher.mail: request.mail,
        Teacher.passwd: request.passwd
    })
    db.commit()
    return {'message': '教員データの更新をしました'}

def update_kougi(db: Session, id: int, request: ArticleCreate):
    kougi = db.query(Kougi).filter(Kougi.id == id)
    kougi.update({
        Kougi.name: request.name,
        Kougi.summary: request.summary
    })
    db.commit()
    return {'message': '講義データの更新をしました'}

# 登録内容削除
def delete_article(db: Session, id: int):
    article = db.query(Article).filter(Article.id == id)
    article.delete()
    db.commit()
    return {'message': 'success'}

def delete_student(db: Session, id: int):
    student = db.query(Student).filter(Student.id == id)
    student.delete()
    db.commit()
    return {'message': '学生データを削除しました'}

def delete_teacher(db: Session, id: int):
    teacher = db.query(Teacher).filter(Teacher.id == id)
    teacher.delete()
    db.commit()
    return {'message': '教員データを削除しました'}

def delete_kougi(db: Session, id: int):
    kougi = db.query(Kougi).filter(Kougi.id == id)
    kougi.delete()
    db.commit()
    return {'message': '講義データを削除しました'}