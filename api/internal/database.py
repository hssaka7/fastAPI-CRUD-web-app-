
from .models import UserInfoIn
from .utility import verify_password


# TODO implement a real db here: sqlite
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


def get_user( username: str):
    if username in fake_users_db:
        user_dict = fake_users_db[username]
        return UserInfoIn(**user_dict)
  
def authenticate_user(username: str, plain_password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(plain_password,user.hashed_password):
        return False
    return user