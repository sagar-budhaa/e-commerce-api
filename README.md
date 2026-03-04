# E-Commerce API

A FastAPI-based REST API for building scalable e-commerce platforms.

## Features

- **Product Management** – Catalog browsing and product administration
- **Shopping Cart** – Add, update, and manage cart items
- **Order Processing** – Complete order workflow and tracking
- **User Authentication** – Secure user registration and login
- **Payment Integration** – Stripe and PayPal support

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or poetry

### Installation

```bash
git clone https://github.com/sagar-budhaa/e-commerce-api.git
cd e-commerce-api
pip install -r requirements.txt
```

### Development

```bash
fastapi dev main.py
```

### Production

```bash
fastapi run main.py
```

The API runs on `http://localhost:8000`

## API Documentation

- **Swagger UI** – `/docs`
- **ReDoc** – `/redoc`

## Project Structure

```
e-commerce-api/
├── main.py                 # Application entry point
├── models/                 # Database models
├── routes/                 # API endpoints
├── schemas/                # Request/response schemas
└── requirements.txt        # Dependencies
```

## Testing

```bash
pip install -r requirements-dev.txt
pytest
```

## License

MIT