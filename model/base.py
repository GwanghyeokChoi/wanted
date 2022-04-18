from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://irpxhsfe:hY97qXOo5pFVm9m0NmN4ovtwpbGFWasl@otto.db.elephantsql.com/irpxhsfe"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()