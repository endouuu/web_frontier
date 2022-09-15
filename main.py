from fastapi import FastAPI
from router import articles, students
from db import models
from db.database import engine
import mysql.connector
import db.database as data
import db.db_article as data_article

app = FastAPI()
# app.include_router(articles.router)
# app.include_router(students.router)

#学生の全データの取得
@app.get('/students', tags=["students"])
async def read_Students():
    result = data.session.query(models.Student).all()
    return result

#個別の学生データの取得
@app.get('/students/{id}', tags=["students"])
async def read_Student(id: int):
    result = data_article.get_student(data.session, id)
    return result

#学生の新規登録
@app.post('/students', tags=["students"])
async def create_student():
    try:
        result = data_article.create_student(data.session, request)
    except:
        data.session.rollback()
        raise  
    finally:
        session.close()

#学生データの削除
@app.delete('/students/{id}', tags=["students"])
async def delete_student(id: int):
    try:
        data_article.delete_student(data.session, id)
    except:
        data.session.rollback()
        raise
    finally:
        session.close()

#学生データの更新
@app.put('/students/{id}', tags=["students"])
async def update_student(id: int):
    try:
        data_article.update_student(data.session, id, request)
    except:
        data.session.rollback()
        raise
    finally:
        session.close()


models.Base.metadata.create_all(engine)