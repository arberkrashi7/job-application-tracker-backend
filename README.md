# Job Application Tracker – Backend Service

Production-style backend service built with FastAPI and async SQLAlchemy.
The service models real-world backend engineering patterns including
authentication, database migrations, pagination, and automated testing.

This project was designed to demonstrate ownership of the full backend
development lifecycle, from API design and data modeling to testing and
deployment.

---

## Tech Stack

- Python
- FastAPI
- Async SQLAlchemy
- PostgreSQL (production) / SQLite (tests)
- Alembic (database migrations)
- Pytest + HTTPX (integration testing)
- Docker & Docker Compose

---

## Architecture Overview

The codebase follows a layered architecture:

- **API layer**: request/response handling and validation
- **Service layer**: business logic and transactional boundaries
- **Persistence layer**: database access via repositories
- **Auth layer**: JWT-based authentication and authorization

This separation improves readability, testability, and long-term
maintainability.

---

## Features

- JWT authentication with protected routes
- Versioned database migrations using Alembic
- CRUD APIs for job applications
- Pagination and filtering for scalable list endpoints
- Async integration tests covering core API flows
- Containerized local development environment

---

## Quickstart (Local)

```bash
pip install -r requirements.txt
alembic upgrade head
pytest
uvicorn app.main:app --reload
```

---

## Additional Notes

```text
Docker:
  docker-compose up --build

Testing:
  pytest

Motivation:
  This project was built to practice designing and implementing a
  production-oriented backend service with an emphasis on correctness,
  data integrity, and long-term maintainability.