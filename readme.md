# Django E-commerce API
This Django project provides a RESTful API for an e-commerce platform. It includes endpoints for managing products, orders, user authentication, and more.

## Features
CRUD operations for products
Ordering and filtering products
Creating and managing orders
User registration, login, and logout
JWT token-based authentication

## Installation
Requirements
Docker
Docker Compose
For unix users
```bash
    chmod +x app/entrypoint.prod.sh
```

Build and run the Docker containers:
```bash
  docker compose -f docker-compose.prod.yml down -v
  docker compose -f docker-compose.prod.yml up -d --build
```
Collect static files:
```bash
  docker compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```
Apply migrations:
```bash
  docker compose -f docker-compose.prod.yml exec web python manage.py migrate
```
Create a superuser (for admin access):
```bash
docker compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

## Usage
Access the API root at http://127.0.0.1:80/swagger/
Explore available endpoints for products, orders, and users
Use tools like Postman or cURL to make requests to the API
Authenticate using JWT tokens:
Obtain tokens at http://127.0.0.1:80/api/token/
Include the token in the Authorization header for protected endpoints
