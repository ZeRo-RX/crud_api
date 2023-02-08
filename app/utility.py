from passlib.context import CryptContext

PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return PASSWORD_CONTEXT.hash(password)


def password_verify(plain_password: str, hashed_password: str):
    return PASSWORD_CONTEXT.verify(plain_password, hashed_password)