# Boarding Pass Parser (IATA BCBP) ✈️

A modular MVP for parsing IATA Bar Coded Boarding Passes (BCBP), built with Python, FastAPI, SQLAlchemy, and Pydantic v2.

---

## 🌟 Key Features

* **IATA BCBP Parser:** Parsing of standard bar-coded boarding pass strings into structured domain models.
* **REST API:** Endpoints for parsing (`POST /api/v1/parse`), fetching listing with filters and pagination (`GET /api/v1/boarding-passes`), and detail lookup (`GET /api/v1/boarding-passes/{id}`).
* **Self-Contained & Zero External Setup:** Uses file-based SQLite database with automatic schema setup upon startup.
* **Minimalist SPA Frontend:** Built-in lightweight UI for interactive Drag & Drop parsing and pass inspection without external JavaScript build tools.
* **Prepared Seed Data:** Automatically populates sample boarding passes for immediate evaluation.
* **Interactive APIDoc:** OpenAPI (Swagger UI) integration available natively at `/docs`.

---

## 🏛️ Architecture Overview

The project follows a **Layered Architecture** separating responsibilities into isolated layers:

* **`backend/core/` (Domain Layer):** Pure IATA parsing logic and Pydantic domain models. Independent of database or API layers.
* **`backend/persistence/` (Data Layer):** SQLAlchemy 2.0 ORM models and Repository pattern encapsulating SQLite interactions.
* **`backend/services/` (Service Layer):** Orchestrates domain logic and persistence.
* **`backend/api/` (Presentation / API Layer):** FastAPI endpoints, request/response validation, and OpenAPI specs.
* **`backend/_setup/` (Bootstrap / Tooling):** Initialization scripts and initial database seeding.
* **`ui/` (Frontend):** Static SPA (HTML/CSS/JS) served directly via FastAPI.
* **`tests/` (Test Suite):** Isolated unit tests for parsing logic and integration tests for REST API endpoints.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Validation & Schemas:** Pydantic v2
* **ORM & Database:** SQLAlchemy 2.0 + SQLite
* **Testing:** Pytest + Pytest-Cov
* **Frontend:** Vanilla JS + Tailwind CSS (via CDN)

---

## 🚀 Quick Start (Install & Run)

### Prerequisites
* Python 3.10 or higher
* Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jan-svezi/kiwi.com.git](https://github.com/jan-svezi/kiwi.com.git)
   cd kiwi.com
   ```

2. **Create and activate a virtual environment:**
   * **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn backend.main:app --reload
   ```

5. **Access the application:**
   * **Web UI (SPA):** Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
   * **Interactive API Documentation (Swagger):** Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## 🧪 Running Tests & Coverage

To run the complete test suite (unit and integration tests) with code coverage report, execute:

```bash
pytest --cov=backend
```

To generate a detailed HTML coverage report:

```bash
pytest --cov=backend --cov-report=html
```

---

## 🔮 Future Architectural Improvements & Production Considerations

* **Database Migrations (Alembic):** For this MVP, database tables are automatically initialized via SQLAlchemy metadata on application startup for zero-dependency execution. In a multi-environment production setup, a database migration tool such as **Alembic** should be introduced to manage schema evolution.
* **Authentication & Authorization:** Add JWT / API Key authentication to protect parser and data retrieval routes.
* **Asynchronous Processing:** For heavy multi-segment PDF decoding, consider offloading processing to asynchronous task queues (e.g., Celery / Redis).
* **Docker Containerization:** Add a multi-stage `Dockerfile` and `docker-compose.yml` for unified container deployment.
* **IATA Boarding Pass Field Expansion:** The current domain models are intentionally trimmed to match the required API response payload. The parser architecture is designed so that additional optional IATA Resolution 792 fields (e.g., security data, baggage allowance, frequent flyer info, fast-track status) can be seamlessly exposed as domain requirements grow.
