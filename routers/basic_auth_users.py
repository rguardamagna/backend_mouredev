from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app=FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str
             

users_db = {
    "rodrigo":{
        "username":"rodridev",
        "fullname":"Rodrigo Guardamagna",
        "email":"rodrigo@algo.com",
        "disabled":False,
        "password":"654321"
    },
    "rodrigo_segundo":{
        "username":"rodridev2",
        "fullname":"Rodrigo Guardamagna 2",
        "email":"rodrigo2@algo.com",
        "disabled":True,
        "password":"6543212"
    }
}

def search_user(username:str):
    for username in users_db:
        return UserDB(users_db[username])

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends() ):
    user_db = user_db.get(form.username)
    if not users_db:
        raise HTTPException(status_code=400, detail="User not found")

    user = search_user(form.username)
    if  not form.password == user.password:
        raise HTTPException(status_code=400, detail="Wrong password")
