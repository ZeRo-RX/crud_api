from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from ..db_connection import Session, get_db
from .. import db_connection, schemas, basemodel, utility, oauth2

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), datab: Session = Depends(get_db)):
    user = datab.query(basemodel.User).filter(
        basemodel.User.mail == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid username or password")

    if not utility.password_verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid username or password")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
