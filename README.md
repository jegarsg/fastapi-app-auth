# FastAPI Auth Microservice

This is an authentication microservice built with **FastAPI** and **PostgreSQL**, structured using **Clean Architecture**, **SOLID principles**, and **CQRS** (Command Query Responsibility Segregation) design pattern.

## ✅ Architecture Highlights

- ✅ **Clean Architecture**: clear separation of concerns between domain, use cases, interfaces, and infrastructure.
- ✅ **SOLID Principles**: modular and maintainable code following industry best practices.
- ✅ **CQRS Pattern**: separation between commands (write operations) and queries (read operations).

## 🚀 Features

- User registration with encrypted password
- Asynchronous PostgreSQL access via SQLAlchemy + asyncpg
- DTO validation using Pydantic
- Modular structure for scalability and testing
- Dockerized for easy local or production deployment

## 🛠️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Alembic
- Docker
- Python 3.11+

## 🏁 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
uvicorn main:app --reload
