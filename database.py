from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Remplace USER, PASSWORD, HOST, PORT, DB_NAME par tes infos
SQLALCHEMY_DATABASE_URL = "postgresql://catalog_user:password123@localhost:5432/product_catalog"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
