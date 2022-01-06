from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog import models, schemas


def create(request: schemas.Blog, db: Session):
    '''Creating A Blog'''
    
    new_blog = models.Blog(title=request.title,
                           body=request.body,
                           user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def fetch_all(db: Session):
    '''Fetching All Blogs'''
    
    blogs = db.query(models.Blog).all()
    return blogs


def update(id: int, request: schemas.Blog, db: Session):
    '''Updating A Blog'''
    
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} is not found')
        
    blog.update({'title': request.title, 
                 'body': request.body}, 
                synchronize_session=False)
    db.commit()
    return 'updated Successfully'


def destroy(id: int, db: Session):
    '''Delete a blog'''
    
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} is not found')
        
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Deleted Successfully'


def fetch(id: int, db: Session):
    '''Fetch a blog'''
    
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} is not found')
    return blog