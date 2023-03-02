
from fastapi import APIRouter,Depends
from .. import  schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db



#add user by sarath on 02/03/2023
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    return user.create(request, db)
   
#show user by sarath on 02/03/2023
@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session=Depends(get_db)) :
    return user.show(id,db)