from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

# blog?limit=10 & public=boolean you can write like this in URL
@app.get("/blog")
def index(limit=10,public:bool=True,sort:Optional[str]=None): #value of public is boolean because you want to check true or false
    if public:
        return {'data': f'{limit} are public from list of blog'}
    else:
        return {'data': f'{limit} from list of blog'}

# why I put unpublished functions on show function.
#  because in fastAPI it exicute code line by line
@app.get("/blog/unpublished")
def unpublished():
    return {'data': {'unpublished'}}


@app.get("/blog/{id}")
def show(id:int):
    # fetch a blog with id
    return {'data':id}

@app.get("/blog/{id}/comments")
def comment(id:int):
    # fetch a blog with comment
    return {'data': {'1','2'}}


class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post("/blog")
def create_blog(request:Blog):
    return {'data':f"blog have title is {request.title} and have body {request.body} created "}












# change port of project

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)