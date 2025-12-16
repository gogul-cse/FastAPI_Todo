from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL =  "sqlite:///./todosapp.db" #"postgresql://postgres:168083@localhost/TodoApplicationDatabase"        #"mysql+pymysql://root:168083@127.0.0.1:3306/TodoApplicationDatabase"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
