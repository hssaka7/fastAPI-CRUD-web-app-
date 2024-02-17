import uvicorn

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from typing import Annotated

from routers import user, post
from internal import login
from internal.login import get_current_user


app  = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(user.router)
app.include_router(post.router)


@app.get("/" )
async def root(token: Annotated[str, Depends(get_current_user)]):
    return {'code':'success', 'message':"Hello World!", 'token': token}

register_tortoise(
    app,
    db_url="sqlite://posts.db",
    modules={"models": ["routers.schema"]},
    generate_schemas=False,
    add_exception_handlers=True,
)
