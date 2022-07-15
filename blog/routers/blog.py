from typing import List
from fastapi import APIRouter, status, Depends
from .. import database, schemas
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blog(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)






