from typing import List
import typing
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm.session import Session
from db import db_article
from db.database import get_db
from db.models import Student
from schemas import StudentCreate, StudentDisplay

router = APIRouter(
    prefix='/student',
    tags=['student']
    )

#学生データ作成
@router.post('/', response_model=StudentDisplay)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return db_article.create_student(db, student)

#全学生データの取得
@router.get('/', response_model=List[StudentDisplay])
def get_students_all(db: Session = Depends(get_db)):
    return db_article.get_students_all(db)

#一学生データの取得
@router.get('/{id}', response_model=StudentDisplay)
def get_student(id: int, db: Session = Depends(get_db)):
    return db_article.get_student(db, id)

#学生データの更新
@router.put('/{id}')
def update_student(id: int, request: StudentCreate, db: Session = Depends(get_db)):
    return db_article.update_student(db, id, request)

#特定の学生データの削除
@router.delete('/{id}')
def delete_student(id: int, db: Session = Depends(get_db)):
    return db_article.delete_student(db, id)