from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MovieModel(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    format = Column(String, nullable=False)
    actors = Column(String, nullable=False)

DATABASE_URL = "sqlite:///./test.db"  # або ваш URL бази даних

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)
