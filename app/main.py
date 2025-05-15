from fastapi import FastAPI
from app.routes import products, sales, inventory
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(inventory.router)
app.include_router(sales.router)
