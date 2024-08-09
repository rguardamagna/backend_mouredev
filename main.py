from fastapi import FastAPI
from routers import users,products
from fastapi.staticfiles import StaticFiles

# auto-generates documentation:
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="statics") , name="static")

@app.get("/")
async def root():
    return "Hola mundo"


@app.get("/url")
async def url():
    return {"url_curso":"https://rodrigo.guardamagna.com/python"}
