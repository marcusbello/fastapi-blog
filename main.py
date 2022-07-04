from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"Blog list"}}


@app.get(f"/blog/{id}")
def get_blog(blog_id: int):
    return {"data": {"Getting blog with id of " + str(blog_id)}}


@app.get("/about")
def about():
    return {"data": {1, 2, 3, 4}}
