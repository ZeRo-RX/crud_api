# import jwt
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from . import schemas, db_connection, basemodel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "tXw7t4xcxXjfG|QrLem>PnWG3ae5-.'1QL<#@Nbv{F#;&tb|{Yb<X>_EMgDDky;"
ALGORITHM = 'HS256'
EXPIRATION_TIME_IN_MINUTES = 30


def create_access_token(data: dict):
    expires = datetime.utcnow() + timedelta(minutes=EXPIRATION_TIME_IN_MINUTES)
    to_encode = data.copy()
    to_encode.update({'exp': expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithm=[ALGORITHM])
        id: str = payload.get('user_id')
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
        return token_data
    except JWTError:
        raise credentials_exception


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db_connection.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="credentials not validated ",
        headers={"WWW-Authenticate": "Bearer"})

    return verify_access_token(token, credentials_exception)
