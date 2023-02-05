from fastapi import FastAPI, Response, status, HTTPException, Depends
from typing import List, Optional
from . import basemodel, schemas
from .db_connection import engine, SessionLocal, Session, get_db

basemodel.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
async def root():
    return {'message': 'Welcome to my API server'}


@app.get('/posts', status_code=status.HTTP_200_OK, response_model=List[schemas.GetPost])
def get_all_posts(datab: Session = Depends(get_db)):
    posts = datab.query(basemodel.Post).all()

    return posts


@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=schemas.PostCreate)
def create_post(n_post: schemas.PostCreate, datab: Session = Depends(get_db)):
    new_post = basemodel.Post(**n_post.dict())
    datab.add(new_post)  # add the new post
    datab.commit()  # push the new changes into database
    datab.refresh(new_post)  # returning post from database

    return new_post


@app.get('/posts/{post_id}', response_model=schemas.GetPost)
def get_post(post_id: int, datab: Session = Depends(get_db)):
    post = datab.query(basemodel.Post).filter(basemodel.Post.id == post_id).first()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with {post_id} doesn't exist.")

    return post


@app.delete('/posts/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, datab: Session = Depends(get_db)):
    deleted_post = datab.query(basemodel.Post).filter(basemodel.Post.id == post_id)
    if not deleted_post.first():  # check if there is not matched id
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with {post_id} doesn't exist.")
    deleted_post.delete(synchronize_session=False)
    datab.commit()  # push the new changes into database

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{post_id}')
def update_post(post_id: int, post: schemas.PostCreate, datab: Session = Depends(get_db)):
    post_query = datab.query(basemodel.Post).filter(basemodel.Post.id == update_id)
    updated_post = post_query.first()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {post_id} doesn't exist.")
    post_query.update(post.dict(), synchronize_session=False)
    datab.commit()  # push the new changes into database

    return post_query.first()


# //////////////////////////////// User Side ////////////////////////////////
@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[schemas.GetUser])
def get_all_users(datab: Session = Depends(get_db)):
    users = datab.query(basemodel.User).all()

    return users


@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.GetUser)
def create_user(n_user: schemas.UserCreate, datab: Session = Depends(get_db)):
    new_user = basemodel.User(**n_user.dict())
    datab.add(new_user)
    datab.commit()
    datab.refresh(new_user)

    return new_user


@app.get('/users/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.GetUser)
def get_user(user_id: int, datab: Session = Depends(get_db)):
    user = datab.query(basemodel.User).filter(basemodel.User.id == user_id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with {get_user_id} doesn't exist.")

    return user
