from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import InventoryOut
from app.crud.inventory import get_all_inventory, get_low_stock_products, update_inventory_quantity

router = APIRouter(prefix="/inventory", tags=["Inventory"])



@router.get("/", response_model=list[InventoryOut])
def list_inventory(db: Session = Depends(get_db)):
    return get_all_inventory(db)

@router.get("/low-stock", response_model=list[InventoryOut])
def list_low_stock_products(db: Session = Depends(get_db)):
    return get_low_stock_products(db)


@router.put("/{product_id}/update-quantity", response_model=InventoryOut)
def update_quantity(product_id: int, new_quantity: int, db: Session = Depends(get_db)):
    inventory = update_inventory_quantity(db, product_id, new_quantity)
    if new_quantity<0:
        raise HTTPException(status_code=400, detail="Quantity cant be negative")
    else:
        return update_inventory_quantity(db, product_id, new_quantity)
