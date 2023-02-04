from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


# ////////////////////////////////
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


# ////////////////////////////////
class GetPost(PostBase):
    # id: int
    created_time: datetime

    class Config:
        orm_mode = True


# ////////////////////////////////
class PostCreate(PostBase):
    pass

    class Config:
        orm_mode = True


# ////////////////////////////////
class PostUpdate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
