from sqlalchemy.orm import Session
from models import Address, Category, Order, Product, Role, User
from schemas import UserCreate, ProductCreate
from auth import hash_password, verify_password

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_password, role=Role.CUSTOMER)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and verify_password(password, user.password):
        return user
    return None


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product(db, product_id)
    if db_product is None:
        return None
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: Category):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category: Category):
    db_category = get_category(db, category_id)
    if db_category is None:
        return None
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if db_category is None:
        return None
    db.delete(db_category)
    db.commit()
    return db_category

def get_order(db: Session, order_id: int, user_id: int):
    return db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: Order, user_id: int):
    total_price = order.quantity * db.query(Product).filter(Product.id == order.product_id).first().price
    db_order = Order(user_id=user_id, product_id=order.product_id, quantity=order.quantity, total_price=total_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int, user_id: int):
    db_order = get_order(db, order_id, user_id)
    if db_order is None:
        return None
    db.delete(db_order)
    db.commit()
    return db_order

def get_address(db: Session, address_id: int, user_id: int):
    return db.query(Address).filter(Address.id == address_id, Address.user_id == user_id).first()

def get_addresses(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Address).filter(Address.user_id == user_id).offset(skip).limit(limit).all()

def create_address(db: Session, address: Address, user_id: int):
    db_address = Address(user_id=user_id, street=address.street, city=address.city, state=address.state, zip_code=address.zip_code)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def update_address(db: Session, address_id: int, address: Address, user_id: int):
    db_address = get_address(db, address_id, user_id)
    if db_address is None:
        return None
    db_address.street = address.street
    db_address.city = address.city
    db_address.state = address.state
    db_address.zip_code = address.zip_code
    db.commit()
    db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: int, user_id: int):
    db_address = get_address(db, address_id, user_id)
    if db_address is None:
        return None
    db.delete(db_address)
    db.commit()
    return db_address
