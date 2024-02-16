
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str|None = None

class UserInfo(BaseModel):
    username: str
    email: str
    full_name: str|None = None
    disabled: bool|None =  None

class UserInfoIn(UserInfo):
    hashed_password: str