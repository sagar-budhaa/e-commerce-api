from fastapi import FastAPI
from database import SessionLocal, engine, Base
from routers import users, products, category, order

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(products.router)
app.include_router(category.router)
app.include_router(order.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce API!", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
