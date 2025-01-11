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
git clone <repository-url>
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

## API Endpoints Doc

Complete API documentation available at /api/docs/

## 🧪 Running Tests

```bash
make test
```
