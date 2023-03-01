from fastapi import FastAPI, Depends,status, Response, HTTPException
from . import schemas,models
from typing import List
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# add blog by id by Sarath on 01/03/2023
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# get all blog by id by Sarath on 01/03/2023
@app.get('/blog',response_model=List[schemas.ShowTitleBlog]) #we can remove response_model=List[schemas.ShowTitleBlog] or change in schemas if we want to see all data
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# delete blog by id by Sarath on 01/03/2023
@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
    blog.delete(synchronize_session=False)

    db.commit()
    return 'deleted'


# update blog by id by Sarath on 01/03/2023
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog ,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
    blog.update({'title':request.title, 'body':request.body})
    db.commit()
    return 'updated'


# get blog by id by Sarath on 01/03/2023
@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,response:Response,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # way 1-------------------
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {'details': f"Blog with the id {id} not available"}
        # way2------------------------
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with the id {id} not available")

    return blog
