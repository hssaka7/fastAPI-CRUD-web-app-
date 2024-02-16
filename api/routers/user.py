from fastapi import  HTTPException, APIRouter
from typing import List
from pydantic import BaseModel

import uvicorn

from .schema import User, Post, User_Pydantic, UserIn_Pydantic

router = APIRouter(prefix="/users",tags=["users"],)

class Status(BaseModel):
    message: str

# CREATE
@router.post("/", response_model= User_Pydantic)
async def create_user(user: UserIn_Pydantic ):
    """Creates a new user"""
    
    user_obj = await User.create(**user.model_dump())
    return await User_Pydantic.from_tortoise_orm(user_obj)

# READ
@router.get("/", response_model=List[User_Pydantic])
async def get_users():
    """Reads the list of all the users"""
    
    all_feed = User.all()
    return await User_Pydantic.from_queryset(all_feed)


@router.get("/user/{id}", response_model=User_Pydantic)
async def get_user(id: int):
    """Reads a single user"""
    
    f_id = User.get(id=id)
    return await User_Pydantic.from_queryset_single(f_id)


# UPDATE
@router.put("/user/{id}", response_model= User_Pydantic)
async def update_user(id: int, user: UserIn_Pydantic):
    """Updates the existing user"""
    
    await User.filter(id=id).update(**user.model_dump())
    return await User_Pydantic.from_queryset_single(User.get(id=id))

#DELETE

@router.delete("/user/{id}", response_model= Status)
async def delete_user(id: int):
    """Deletes the existing user"""
    
    count = await User.filter(id=id).delete()

    if not count:
        raise HTTPException(status_code=404, detail=f"User {id} not found")

    return Status(message=f"Deleted user {id}") 


