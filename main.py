from fastapi import FastAPI, Depends
from api.routes import auth_routes
from core import initialization
from api.utils import auth_util
from api.models.user import User

app = FastAPI()

app.include_router(auth_routes.router, prefix="/api/v1/auth")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/user")
async def say_hello(user: User = Depends(auth_util.get_current_user)):
    return {"message": f"Hello {user.full_name}"}


@app.on_event("startup")
def on_startup():
    initialization.init()
