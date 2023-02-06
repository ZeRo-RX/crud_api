from sqlalchemy import create_engine
from . import basemodel
from sqlalchemy.orm import sessionmaker, Session, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost/CRUD_API"
# SQLALCHEMY_DATABASE_URL = "postgresql://<USERNAME>:<PASSWORD>@<HOST_or_IP>/<DATABASE_NAME>"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
