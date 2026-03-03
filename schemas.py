from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserRead


class ProductBase(BaseModel):
    name: str
    description: str = None
    price: float

class ProductCreate(ProductBase):
    pass


class CategoryBase(BaseModel):
    name: str

class OrderBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float
