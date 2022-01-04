from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blogs')
def index(limit=10, published : bool=True, sort : Optional[str] = None):
    # only gets 10 published blogs
    
    if published:
        return {'data':f'{limit} published Blog list from db'}
    else:
        return f'{limit} blog list from db'

@app.get('/blog/unpublished')
def unpublished():
    # return unpublished blogs
    
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id : int):
    # fetch blog with id = id
    
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id

    return {'data': ['1','2']}

class Blog(BaseModel):
    # Blog Model
    
    title : str
    body : str
    published : Optional[bool]
    
    
@app.post('/blog')
def create_blog(blog : Blog):
    return {'data': blog}


# For Debuging Purpose
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)