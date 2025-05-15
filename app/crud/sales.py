from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Sale
from datetime import datetime




def get_sales(db: Session, start_date: datetime, end_date: datetime):
    query = db.query(Sale)
    if start_date:
        query = query.filter(Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(Sale.sale_date <= end_date)
    return query.all()


def get_revenue_summary(db:Session,group_by:str="day"):
    group_formats ={
        "day": "%Y-%m-%d",
        "month": "%Y-%m",
        "year": "%Y"
    }
    if group_by not in group_formats:
        group_by = "day"
    
    date_format = group_formats[group_by]

    return db.query(
        func.date_format(date_format, Sale.sale_date).label("period"),
        func.sum(Sale.sale_price * Sale.quantity).label("total_revenue"),
    ).group_by("period").order_by("period").all()

def compare_revenue(db: Session, start1: datetime, end1: datetime, start2: datetime, end2: datetime):
    rev1 = db.query(func.sum(Sale.sale_price * Sale.quantity)).filter(Sale.sale_date.between(start1, end1)).scalar() or 0
    rev2 = db.query(func.sum(Sale.sale_price * Sale.quantity)).filter(Sale.sale_date.between(start2, end2)).scalar() or 0
    return {"period_1": rev1, "period_2": rev2}
