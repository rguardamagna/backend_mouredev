from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["user","users"])

# Entidad user
class User(BaseModel):
    id:int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="rodrigo",surname="guardamagna",url="https://rodrigoguardamagna.com",age=35),
            User(id=2,name="esther",surname="piscore",url="https://estherpiscore.com",age=65),
            User(id=3,name="dale",surname="messi",url="https://traemelacopa.com",age=34)]

def search_user(id:int):
    users=filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}
    
@router.get("/usersjson")
async def usersjson():
    return [{"name":"rodrigo","surname":"guardamagna","url":"https://rodrigoguardamagna.com"},
            {"name":"esther","surname":"piscore","url":"https://estherpiscore.com"},
            {"name":"dale","surname":"messi","url":"https://traemelacopa.com"}]


@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

@router.get("/user/")
async def user(id: int):
    return search_user(id)

@router.get("/userquery/")
async def user(id: int):
    return search_user(id)

@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):

        if type(search_user(user.id)) == User:
            raise HTTPException(status_code=204,detail="El usuario ya existe")

        users_list.append(user)
        return user

@router.put("/user/")
async def user(user: User):
    try:
        found=False
        for index,saved_user in enumerate(users_list):
            if saved_user.id == user.id:
                users_list[index] = user
                found=True

        if not found:
            {"error":"no se ha encontrado el usuario"}
        return user
            
    except:
        pass

@router.delete("/user/{id}")
async def user(id:int):
    found=False
    for index,saved_user in enumerate(users_list):
        if saved_user.id == id:
                del users_list[index]
                found=True
    if not found:
        return {"error":"no se ha eliminado el usuario"}
        


