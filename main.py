
from fastapi import FastAPI

import model
from database import engine
from routers import blog, user

model.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)


