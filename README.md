# 🚀 FastAPI Auth Microservice

This is an authentication microservice built with **FastAPI** and **PostgreSQL**, structured using **Clean Architecture**, **SOLID principles**, and the **CQRS (Command Query Responsibility Segregation)** design pattern.

---

## ✅ Architecture Highlights

- 🧱 **Clean Architecture** – Clear separation of concerns between domain, use cases, interfaces, and infrastructure.
- 🧩 **SOLID Principles** – Modular and maintainable code following industry best practices.
- ⚡ **CQRS Pattern** – Clear split between Commands (write) and Queries (read).

---

## 🚀 Features

- 🔐 User registration with encrypted password
- ⚡ Async PostgreSQL access via SQLAlchemy + asyncpg
- ✅ DTO validation using Pydantic
- 📦 Modular structure for scalability and testing
- 🐳 Dockerized for local/production deployment

---

## 🛠️ Tech Stack

- **Python** 3.11+
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy** (async)
- **Alembic**
- **Docker**

---

## 🏁 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

---

## 📂 Project Structure (Clean Architecture)
```bash
app/
├── core/                            # App-wide configuration
│   └── config.py
│
├── infrastructure/                 # External services & data sources
│   └── database/
│       ├── models/                 # SQLAlchemy models (ORM)
│       │   └── user_model.py
│       ├── base.py
│       └── session.py
│
├── modules/
│   └── user/
│       ├── commands/               # Write operations (CQRS)
│       │   ├── handlers/
│       │   │   └── register_user_handler.py
│       │   ├── validators/
│       │   │   └── register_user_validator.py
│       │   └── register_user_command.py
│       │
│       ├── queries/                # Read operations (CQRS)
│       │   ├── handlers/
│       │   │   └── get_user_by_email_handler.py
│       │   └── get_user_query.py
│       │
│       ├── controllers/            # FastAPI route handlers
│       │   └── user_controller.py
│       │
│       ├── dtos/                   # Request/response models
│       │   └── user_dto.py
│       │
│       ├── repository/             # Data access layer (abstracted)
│       │   └── user_repository.py
│       │
│       ├── services/               # Domain/business logic
│       │   └── user_service.py
│       │
│       └── utils/                  # Module-specific helpers
│           └── user_utils.py
│
├── shared/                         # Shared logic across modules
│   ├── db_dependency.py
│   ├── exceptions.py
│   └── utils/
│       ├── encryption.py
│       └── string_generator.py
│
├── main.py                         # App entry point
└── .env                            # Environment configuration

```

---

## 📄 LICENSE

MIT