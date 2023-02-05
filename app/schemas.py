from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


# ////////////////////////////////
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class GetPost(PostBase):
    # id: int
    created_time: datetime

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass

    class Config:
        orm_mode = True


class PostUpdate(PostBase):
    pass


# //////////////////////////////// User Side ////////////////////////////////
class UserBase(BaseModel):
    mail: EmailStr

    class Config:
        orm_mode = True


class GetUser(UserBase):
    id: int
    created_time: datetime

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True
