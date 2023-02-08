from fastapi import FastAPI
from . import basemodel
from .db_connection import engine
from .routers import post, user, authentication

basemodel.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(authentication.router)


@app.get('/')
async def root():
    return {'message': 'Welcome to my API server'}

