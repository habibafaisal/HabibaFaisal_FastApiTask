from app.models import Product
from app.schemas import ProductCreate
from sqlalchemy.orm import Session

def create_product(db:Session,product:ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_all_product(db:Session):
    return db.query(Product).all()