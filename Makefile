.PHONY: help build up down logs test shell migrate dev prod clean

help:
    @echo "Available commands:"
    @echo "build  - Build Docker images"
    @echo "up     - Start development services"
    @echo "down   - Stop all services"
    @echo "logs   - View logs"
    @echo "test   - Run tests"
    @echo "shell  - Open Django shell"
    @echo "migrate- Run migrations"
    @echo "dev    - Start development environment"
    @echo "prod   - Start production environment"
    @echo "clean  - Remove all containers and images"

build:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml build

up:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml up

down:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml down

logs:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml logs -f

test:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml run --rm web pytest

shell:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml run --rm web python manage.py shell

migrate:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml run --rm web python manage.py migrate

dev:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.dev.yml up --build

prod:
    docker compose -f docker/compose/compose.yml -f docker/compose/compose.prod.yml up --build -d

clean:
    docker compose -f docker/compose/compose.yml down -v --rmi all