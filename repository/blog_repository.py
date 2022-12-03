from starlette import status
from fastapi import Response, HTTPException

import model
from sqlalchemy.orm import Session

from database import get_db


def get_all(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs


def show(db: Session, post_id: int, response: Response):
    blog = db.query(model.Blog).filter(model.Blog.id == post_id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'details': "Post not found"}
    return blog


def create(request, db):
    new_blog = model.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {'data': new_blog, 'message': "added"}


def destroy(post_id, response, db):
    blog = db.query(model.Blog).filter(model.Blog.id == post_id).delete(synchronize_session=False)
    db.commit()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
    return {'details': "Post not found"}
    return {'data': {'message': "deleted"}}
