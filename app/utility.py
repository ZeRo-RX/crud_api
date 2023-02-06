from passlib.context import CryptContext

PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return PASSWORD_CONTEXT.hash(password)
