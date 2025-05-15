from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from app.database import get_db
from app.crud.sales import get_sales, get_revenue_summary, compare_revenue

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.get("/")
def fetch_sales(
    db: Session = Depends(get_db),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    return get_sales(db, start_date, end_date)

@router.get("/revenue/")
def revenue_summary(
    db: Session = Depends(get_db),
    group_by: Optional[str] = Query("day", enum=["day", "month", "year"])
):
    return get_revenue_summary(db, group_by)

@router.get("/compare/")
def revenue_comparison(
    db: Session = Depends(get_db),
    start1: datetime = Query(...),
    end1: datetime = Query(...),
    start2: datetime = Query(...),
    end2: datetime = Query(...)
):
    return compare_revenue(db, start1, end1, start2, end2)
