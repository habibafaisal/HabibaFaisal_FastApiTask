from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    inventory = relationship('Inventory', back_populates='product',uselist=False)
    sales = relationship('Sale', back_populates='product')

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    updated_at = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="inventory")

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    sale_price = Column(Float)
    sale_date = Column(DateTime, default=datetime.utcnow)

    product = relationship('Product', back_populates='sales')