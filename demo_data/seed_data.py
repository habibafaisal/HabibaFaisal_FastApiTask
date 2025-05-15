from faker import Faker
from sqlalchemy.orm import Session
from app.models import Product, Sale, Inventory
from app.database import SessionLocal
import random
from datetime import datetime, timedelta

fake = Faker()
db: Session = SessionLocal()

categories = ["Electronics", "Home", "Beauty", "Toys"]

for _ in range(20):
    product = Product(
        name=fake.word().capitalize() + " " + fake.word().capitalize(),
        category=random.choice(categories),
        price=round(random.uniform(10, 1000), 2),
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    db.add(Inventory(product_id=product.id, quantity=random.randint(5, 100)))
    
    for _ in range(random.randint(3, 10)):
        db.add(Sale(
            product_id=product.id,
            quantity=random.randint(1, 5),
            sale_price=product.price * random.uniform(0.9, 1.1),
            sale_date=fake.date_time_between(start_date='-6M', end_date='now')
        ))

db.commit()
db.close()
