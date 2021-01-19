import time

from datetime import timedelta
from typing import Optional

from fastapi import FastAPI, HTTPException, status

from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from passlib.context import CryptContext
from pydantic import BaseModel

#import os; os.urandom(32).hex() 生成密钥
SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

from fastapi_login import LoginManager
manager = LoginManager(SECRET, tokenUrl='/token')

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@manager.user_loader
def load_user(username: str):  # could also be an asynchronous function
    user = fake_users_db.get(username)
    return UserInDB(**user)

@app.post('/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = load_user(username)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif not verify_password(password, user.hashed_password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=user.username), 
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get("/users/me/", response_model=User)
def read_users_me(current_user: User=Depends(manager)):
    return current_user

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    print(request.method, request.url, request.url.path, request.client.host)
    print([x.endpoint.__name__ for x in request.app.routes if x.path == request.url.path])

    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response