from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
def index():
    return {'data': {'blog list'}}

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


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)