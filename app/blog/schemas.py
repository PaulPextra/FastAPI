from pydantic import BaseModel
from typing import List, Optional

# schemas.py file houses the pydantic models #

class BlogBase(BaseModel):
    '''Blog Schema'''
    
    title: str
    body: str
    
class Blog(BlogBase):
    '''BlogBase Schema'''
    
    class Config():
        orm_mode = True


class User(BaseModel):
    '''User Schema'''
    
    name: str
    email: str
    password: str
    
class ShowUser(BaseModel):
    '''ShowUser Schema''' 
    
    name : str
    email : str
    blogs : List[Blog] = []
    
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    '''ShowBlog Schema'''
    
    title: str
    body: str
    creator: ShowUser
    
    class Config():
        orm_mode = True

class Login(BaseModel):
    '''Login Schema'''
    
    username: str
    password: str
    

class Token(BaseModel):
    '''JWToken Schema'''
    
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None