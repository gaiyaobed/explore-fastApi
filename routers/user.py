from fastapi import FastAPI, Depends, APIRouter

from sqlalchemy.orm import Session

import hasging
import model
import schema
from database import get_db

router = APIRouter()


@router.post('/user', status_code=201, response_model=schema.ShowUser, tags=['users'])
def create_user(request: schema.User, db: Session = Depends(get_db)):
    hash_password = hasging.hash_password(request.password)
    new_user = model.User(name=request.name, email=request.email, password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post('/login', status_code=201, tags=['users'])
def login(request: schema.User, db: Session = Depends(get_db)):
    return request
