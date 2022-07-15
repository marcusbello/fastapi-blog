# import uvicorn
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, SessionLocal
from typing import List
from .hashing import Hash
from .routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


# debug
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=3080)
