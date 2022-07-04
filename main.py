from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the bd'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'data': 'Getting blog with id of ' + str(id)}


@app.get('/blog/{id}/comments')
def get_blog_comments(id: int):
    return {'data': 'Getting comments of blog with id of ' + str(id)}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'blog created is created with title as {request.title}'}


@app.get('/about')
def about():
    return {'data': {1, 2, 3, 4}}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3080)