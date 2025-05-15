from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models import Inventory, Product
from datetime import datetime

LOW_STOCK_THRESHOLD = 10


def get_all_inventory(db: Session):
    return db.query(Inventory).all()


def get_low_stock_products(db: Session):
    return db.query(Inventory).filter(Inventory.quantity < LOW_STOCK_THRESHOLD).all()


def update_inventory_quantity(db:Session,product_id:int,new_quantity:int):
    inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if inventory:
        inventory.quantity = new_quantity
        inventory.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(inventory)
        return inventory
    else:
        return None
    
