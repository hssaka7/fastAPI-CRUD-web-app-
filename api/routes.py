from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from typing import List

import uvicorn

from schema import User, Post, User_Pydantic

app = FastAPI()

@app.get("/")
async def root():
    return {'code':'success', 'message':"Hello World!"}

@app.get("/users", response_model=List[User_Pydantic])
async def get_feeds():
    all_feed = User.all()
    return await User_Pydantic.from_queryset(all_feed)

@app.get("/users/{id}", response_model=User_Pydantic)
async def get_feed(id: int):
    f_id = User.get(id=id)
    return await User_Pydantic.from_queryset_single(f_id)


register_tortoise(
    app,
    db_url="sqlite://posts.db",
    modules={"models": ["schema"]},
    generate_schemas=False,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    uvicorn.run('routes:app', host='127.0.0.1', port=8000, reload=True)
