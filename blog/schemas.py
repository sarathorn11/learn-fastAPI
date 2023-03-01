from pydantic import BaseModel


class Blog(BaseModel):
    title:str
    body:str


# create model /// ShowBlog(Blog) is ment ShowBlog is extended from Blog
class ShowBlog(Blog):
    class Config():
        orm_mode = True

class ShowTitleBlog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True