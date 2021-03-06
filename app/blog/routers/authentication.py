from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. hashing import Hash
from .. import schemas, database, models, token

router = APIRouter(
    tags = ['Authentication']
)

get_db = database.get_db

# Router for User authentication
@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Invalid Credentials')
        
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Incorrect password')
        
    # generate jwt token and return
    access_token = token.create_access_token(
        data = {"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}