from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    name:str
    category:str
    price:float

class ProductOut(ProductCreate):
    id:int
    created_at: datetime
    class Config:
        from_attributes = True

class SaleCreate(BaseModel):
    product_id:int
    quantity:int
    sale_price:float

class InventoryUpdate(BaseModel):
    quantity:int


class InventoryOut(BaseModel):
    product_id:int
    quantity:int
    updated_at:datetime
    class Config:
        from_attributes = True