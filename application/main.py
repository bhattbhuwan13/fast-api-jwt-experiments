"""FastAPI starter sample
"""

from fastapi import FastAPI

app = FastAPI()

from application.model import PostSchema

posts = [
    {"id": 1, "title": "Penguins", "content": "Penguins are flightless birds"},
    {
        "id": 2,
        "title": "Tigers",
        "content": "Tigers belong to the panthera family",
    },
    {"id": 3, "title": "Koala", "content": "Koala is a herbivores animal"},
]

users = []


@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}


# Get all posts
@app.get("/posts", tags=["posts"])
def get_post():
    return {"data": posts}


# Get single post
@app.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {"error": "Post with the given id does not exists"}
    for post in posts:
        if post["id"] == id:
            return {"data": post}


# Post a single blog
@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"info": "post added"}
