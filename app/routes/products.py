from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ProductCreate, ProductOut
from app.crud.products import create_product, get_all_product




router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductOut)
def register_product(product:ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return get_all_product(db)