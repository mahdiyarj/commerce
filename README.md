# Commerce API

A modern e-commerce REST API built with Django REST Framework.

## 🚀 Features

- RESTful API architecture
- JWT Authentication
- PostgreSQL database
- MinIO for file storage
- Docker containerization
- Separate development and production environments
- API filtering and pagination
- Comprehensive test suite

## 🛠️ Tech Stack

- Python 3.13
- Django & Django REST Framework
- PostgreSQL
- MinIO Object Storage
- Docker & Docker Compose
- pytest for testing

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/mahdiyarj/commerce.git
cd commerce
```

2. Copy environment files:

```bash
cp docker/.env/.env.example docker/.env/.dev
cp docker/.env/.env.example docker/.env/.prod
```

3. Update environment variables in .env/.dev and .env/.prod

## 🚀 Running the Application

Development

```bash
make dev
```

Production

```bash
make prod
```

## 🔧 Available Make Commands

- make build - Build Docker images
- make up - Start development services
- make down - Stop all services
- make logs - View logs
- make test - Run tests
- make shell - Open Django shell
- make migrate - Run migrations
- make clean - Remove all containers and images

## 🔗 API Endpoints

### Authentication

- `POST /users/register/` - Register new user
- `POST /users/login/` - Obtain JWT token
- `POST /users/logout/` - Blacklist JWT token
- `GET /users/profile/` - Get user profile
- `PUT /users/profile/` - Update entire profile
- `PATCH /users/profile/` - Partially update profile

### Products

- `GET /sales/products/` - List all products
- `POST /sales/products/` - Create new product (admin only)
- `GET /sales/products/{id}/` - Get product details
- `PUT /sales/products/{id}/` - Update product (admin only)
- `DELETE /sales/products/{id}/` - Delete product (admin only)

### Product Images

- `GET /sales/products/{id}/images/` - List product images
- `POST /sales/products/{id}/images/` - Add product image

### Invoices

- `GET /sales/invoices/` - List user invoices
- `POST /sales/invoices/` - Create new invoice
- `GET /sales/invoices/{id}/` - Get invoice details

### Invoice Items

- `GET /sales/invoices/{invoice_id}/items/` - List invoice items
- `POST /sales/invoices/{invoice_id}/items/` - Add item to invoice

### Transactions

- `GET /sales/transactions/` - List user transactions
- `POST /sales/transactions/` - Create new transaction

### API Documentation

- `GET /api/docs/` - Swagger UI documentation
- `GET /api/schema/` - OpenAPI schema

## 🧪 Running Tests

```bash
make test
```
