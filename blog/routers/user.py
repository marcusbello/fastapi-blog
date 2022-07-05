from typing import List
from fastapi import APIRouter, status, HTTPException, Depends
from .. import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowUser])
def all_user(db: Session = Depends(get_db)):
    return user.all(db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

