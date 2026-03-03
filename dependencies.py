from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import oauth2_scheme, decode_access_token
from database import SessionLocal
from models import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_access_token(token)
    print(f"Decoded user ID from token: {user_id}")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return db.query(User).filter(User.id == user_id).first()
