"""
Assignment
Here is your opportunity to keep learning!
1. Create a new route called Users.
2. Then create 2 new API Endpoints
get_user: this endpoint should return all information about the user that is currently logged in.
change_password: this endpoint should allow a user to change their current password.
"""
from fastapi import Depends, HTTPException, APIRouter
from passlib.context import CryptContext
from pydantic import BaseModel,Field
from sqlalchemy.orm import Session
from starlette import status

from ..model import  Users
from typing import Annotated
from ..database import  SessionLocal
from .auth import get_current_user

router = APIRouter(prefix="/users",
                   tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield  db
    finally:
        db.close()

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/",status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency,user:user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Authentication Failed")
    return db.query(Users).all()


@router.put("/change_password",status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user:user_dependency,db:db_dependency,
                          user_verification:UserVerification):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Authentication Failed")
    user_model = db.query(Users).filter(Users.id==user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail="Password Changed")
    user_model.hashed_password = bcrypt_context.encrypt(user_verification.password)
    db.add(user_model)
    db.commit()


"""
Here is your opportunity to keep learning!
Let's enhance our application again using Alembic! :)
Add a phone number field as required when we create a new user within our auth.py file
Create a new @put request in our users.py file that allows a user to update their phone_number
"""

@router.put("/update_phone_number/{phone_number}",status_code=status.HTTP_204_NO_CONTENT)
async def update_phone_number(user:user_dependency,db:db_dependency,phone_number:str):
    if user is None:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Authentication Failed")
    user_model = db.query(Users).filter(Users.id==user.get('id')).first()

    user_model.Phone_number = phone_number
    db.add(user_model)
    db.commit()