from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import schemas, database
from blog.repository import user

router = APIRouter(
    prefix = '/user',
    tags = ['Users']
)

get_db = database.get_db

# Router for Creating a user 
@router.post('/', 
          status_code=status.HTTP_201_CREATED, 
          response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    
    return user.create(request, db)

# Router for Fetching user
@router.get('/{id}', 
         status_code=status.HTTP_200_OK, 
         response_model=schemas.ShowUser)
def fetch_user(id: int, db: Session=Depends(get_db)):
    
    return user.fetch(id, db)