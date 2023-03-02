from pydantic import BaseModel
from typing import List

 

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class Config():
        orm_mode = True




class ShowTitleBlog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog]=[]
    class Config():
        orm_mode = True

# create model /// ShowBlog(Blog) is ment ShowBlog is extended from Blog
class ShowBlog(Blog):
    creator: ShowUser
    class Config():
        orm_mode = True