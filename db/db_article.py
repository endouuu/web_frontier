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

# 全ての登録情報を確認
def get_articles_all(db: Session):
    return db.query(Article).filter(Article.is_display == True).all()

# 登録内容情報確認
def get_article(db: Session, id: int):
    return db.query(Article).filter(Article.id == id).first()

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

# 登録内容削除
def delete_article(db: Session, id: int):
    article = db.query(Article).filter(Article.id == id)
    article.delete()
    db.commit()
    return {'message': 'success'}