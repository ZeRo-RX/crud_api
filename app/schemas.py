from pydantic import BaseModel, EmailStr
from datetime import datetime


class PostDefault(BaseModel):  # default post get dictionary
    title: str
    content: str
    published: bool = True


class CreatePost(PostDefault):  # default post create dictionary
    pass


class Post(PostDefault):  # default post update dictionary
    id: int

    class Config:
        orm_mode = True


class PostReturn(PostDefault):
    id: int
    created_time: datetime

    class Config:  # ignore if not dictionary
        orm_mode = True


class UserCreate(BaseModel):
    mail: EmailStr
    password: str
