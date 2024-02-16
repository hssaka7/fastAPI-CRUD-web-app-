from fastapi import APIRouter, HTTPException
from .schema import Post, Post_Pydantic, User,User_Pydantic, PostIn_Pydantic
from typing import List
from pydantic import BaseModel
from tortoise.query_utils import Prefetch

router = APIRouter(prefix='/post', tags=['posts'])

class Status(BaseModel):
    message: str



# CREATE
@router.post("/", response_model= PostIn_Pydantic)
async def create_post(user_id:int, post: PostIn_Pydantic):
    """Create a post"""
    
    user = await User.get(id = user_id)
    post_obj = await Post.create(**post.model_dump(), user=user)
    return await Post_Pydantic.from_tortoise_orm(post_obj)


# READ
@router.get("/", response_model= List[User_Pydantic])
async def get_posts(user_id: int):
    """Read all posts"""

    all_post = User.filter(id=user_id)
    return await User_Pydantic.from_queryset(all_post)


@router.get("/{post_id}", response_model = PostIn_Pydantic)
async def get_post(user_id: int, post_id: int):
    """Read single post"""
    return  await PostIn_Pydantic.from_queryset_single(Post.get(id=post_id))


# UPDATE
@router.put("/{post_id}", response_model= PostIn_Pydantic)
async def update_post(user_id: int, post_id: int, post: PostIn_Pydantic):
    """Updates a post"""

    await Post.filter(id=post_id, user_id=user_id).first().update(** post.model_dump())
    return PostIn_Pydantic.from_queryset(Post.Filter(id=post_id, user_id=user_id).first())

# DELETE
@router.delete("/{post_id}", response_model= Status)
async def delete_post(user_id: int, post_id: int):
    """Deletes a post"""
    count = await Post.filter(id = post_id, user_id = id).first().delete()
    if not count:
        raise HTTPException(status_code=404, detail=f"Post {post_id} not found")

    return Status(message=f"Deleted post {post_id}") 






# @router.post("/{user_id}", response_model=Post_Pydantic)
# async def create_post(user_id:int, user: Post_Pydantic):
#     pass



# @router.get("/{user_id}/{post_id}", response_model=Post_Pydantic)
# async def get_post(user_id: int, post_id: int):
#     pass

# @router.put("{user_id}/{post_id}",response_model=Post_Pydantic)
# async def update_post(user_id: int, post_id: int, post:Post_Pydantic):
#     pass

# @router.delete("/{user_id}/{post_id}", response_class= Status)
# async def delete_post(user_id:int, post_id: int):
#     pass