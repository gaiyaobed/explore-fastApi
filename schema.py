from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    email: str
    name: str
    class Config:
        orm_mode = True
