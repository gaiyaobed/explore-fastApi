from fastapi import APIRouter

from fastapi import Depends, Response, HTTPException

from sqlalchemy.orm import Session
from starlette import status

import model
import schema
from database import get_db

from repository import blog_repository

router = APIRouter(prefix="/api/v1/blogs", tags=["blogs"], )


@router.get("/blog", status_code=status.HTTP_200_OK)
def fetch_blogs(db: Session = Depends(get_db)):
    return blog_repository.get_all(db)


@router.get("/blog/{post_id}", status_code=200)
def show(post_id: int, response: Response, db: Session = Depends(get_db)):
    return blog_repository.show(db, post_id, response)


@router.delete("/blog/{post_id}", status_code=200)
def destroy(post_id: int, response: Response, db: Session = Depends(get_db)):
    return blog_repository.destroy(post_id, response, db)


@router.put("/blog/{post_id}", status_code=201)
def update(post_id: int, response: Response, request: schema.Blog, db: Session = Depends(get_db)):
    post = db.query(model.Blog).filter(model.Blog.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not found')

    post.update(request)
    db.commit()
    return {'data': 'post'}


@router.post('/blog', status_code=status.HTTP_201_CREATED)
async def create(request: schema.Blog, db: Session = Depends(get_db)):
    return blog_repository.create(request, db)
