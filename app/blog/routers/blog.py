from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from blog.oauth2 import get_current_user
from blog import schemas, database, oauth2
from blog.repository import blog


router = APIRouter(
    prefix = '/blog',
    tags = ['Blogs']
)

get_db = database.get_db

get_current_user = oauth2.get_current_user

# Router for Creating a blog
@router.post('/', 
          status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return blog.create(request, db)


# Router for Fetching all blogs 
@router.get('/', 
         status_code=status.HTTP_200_OK, 
         response_model=List[schemas.ShowBlog])
def fetch_all_blogs(db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return blog.fetch_all(db)


# Router for Updating a blog
@router.put('/{id}', 
         status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return blog.update(id, request, db)


# Router for Deleting a blog 
@router.delete('/{id}', 
            status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return blog.destroy(id, db)


# Router for Fetching blog
@router.get('/{id}', 
         status_code=status.HTTP_200_OK, 
         response_model=schemas.ShowBlog)
def fetch_blog(id, db: Session=Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    return blog.fetch(id, db)