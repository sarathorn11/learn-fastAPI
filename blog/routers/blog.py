from fastapi import APIRouter,Depends,status
from typing import List
from .. import  schemas, database
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db


# get all blog by id by Sarath on 01/03/2023
@router.get('/',response_model=List[schemas.ShowTitleBlog]) #we can remove response_model=List[schemas.ShowTitleBlog] or change in schemas if we want to see all data
def all(db:Session = Depends(get_db)):
    return blog.get_all(db)


# add blog by id by Sarath on 01/03/2023
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db: Session = Depends(get_db)):
    return blog.create(request,db)



# delete blog by id by Sarath on 01/03/2023
@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db)):
    return blog.destroy(id,db)


# update blog by id by Sarath on 01/03/2023
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.Blog ,db:Session = Depends(get_db)):
    return blog.update(id,request,db)


# get blog by id by Sarath on 01/03/2023
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,db:Session = Depends(get_db)):
    return blog.show(id,db)
