from fastapi import FastAPI, Response, status, HTTPException, Depends

from . import basemodel, schemas
from .db_connection import engine, SessionLocal, Session, get_db

basemodel.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
async def root():

    return {'message': 'Welcome to my API server'}


@app.get('/posts', status_code=status.HTTP_200_OK)
def get_posts(datab: Session = Depends(get_db)):
    posts = datab.query(basemodel.Post).all()

    return {'data': posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(n_post: schemas.CreatePost, datab: Session = Depends(get_db)):
    new_post = basemodel.Post(**n_post.dict())
    datab.add(new_post)  # add the new post
    datab.commit()  # push the new changes into database
    datab.refresh(new_post)  # returning post from database

    return {'data': new_post}


@app.get('/posts/{get_id}', status_code=status.HTTP_200_OK)
def get_post(get_id: int, datab: Session = Depends(get_db)):
    post = datab.query(basemodel.Post).filter(basemodel.Post.id == get_id).first()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with {get_id} doesn't exist.")

    return {'data': post}


@app.delete('/posts/{delete_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(delete_id: int, datab: Session = Depends(get_db)):
    deleted_post = datab.query(basemodel.Post).filter(basemodel.Post.id == delete_id)
    if not deleted_post.first():  # check if there is not matched id
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"post with {delete_id} doesn't exist.")
    deleted_post.delete(synchronize_session=False)
    datab.commit()  # push the new changes into database

    return {'data': deleted_post}


@app.put('/posts/{update_id}', status_code=status.HTTP_200_OK)
def update_post(update_id: int, post: schemas.PostDefault , datab: Session = Depends(get_db)):
    post_query = datab.query(basemodel.Post).filter(basemodel.Post.id == update_id)
    updated_post = post_query.first()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {update_id} doesn't exist.")
    post_query.update(post.dict(), synchronize_session=False)
    datab.commit()  # push the new changes into database

    return {'data': post_query.first()}


