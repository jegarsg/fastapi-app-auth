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
│
├── modules/
│   └── user/
│       ├── commands/               # Write operations (CQRS)
│       │
│       ├── queries/                # Read operations (CQRS)
│       │
│       ├── controllers/            # FastAPI route handlers
│       │
│       ├── dtos/                   # Request/response models
│       │
│       ├── repository/             # Data access layer (abstracted)
│       │
│       ├── services/               # Domain/business logic
│       │
│       └── utils/                  # Module-specific helpers
│
├── shared/                         # Shared logic across modules
│
├── main.py                         # App entry point
└── .env                            # Environment configuration

```

---

## 📄 LICENSE

MIT
