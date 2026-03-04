from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_current_user
import crud, schemas
from database import SessionLocal

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.OrderBase)
def create_order(order: schemas.OrderCreate, current_user: schemas.UserRead = Depends(get_current_user), db: Session = Depends(get_db)):
    print(current_user)
    user_id = current_user.id
    db_order = crud.create_order(db, order, user_id=user_id)
    return db_order

@router.get("/{order_id}", response_model=schemas.OrderBase)
def read_order(order_id: int, current_user: schemas.UserRead = Depends(get_current_user), db: Session = Depends(get_db)):
    user_id = current_user.id
    db_order = crud.get_order(db, order_id=order_id, user_id=user_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.get("/", response_model=list[schemas.OrderBase])
def read_orders(skip: int = 0, limit: int = 100, db:
    Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

@router.delete("/{order_id}", response_model=schemas.OrderBase)
def delete_order(order_id: int, current_user: schemas.UserRead = Depends(get_current_user), db: Session = Depends(get_db)):
    user_id = current_user.id
    db_order = crud.delete_order(db, order_id, user_id=user_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order