from database import engine, Base
from models import Product

Base.metadata.create_all(bind=engine)
print("Tables créées avec succès !")
