# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Electricity Usage-Based CO₂ Emission Monitoring Backend — a FastAPI service that ingests electricity usage telemetry, calculates CO₂ emissions (fixed factor: 0.233 kg CO₂/kWh), and stores results in SQLite.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run dev server (auto-reload)
uvicorn main:app --reload

# Run tests
pytest

# Run a single test
pytest path/to/test_file.py::test_function_name
```

## Architecture

Layered architecture with three tiers:

- **Routers** (`routers/readings.py`) — FastAPI route handlers, parameter validation, HTTP concerns
- **Services** (`services/readings_service.py`) — Business logic, CO₂ calculation, database queries with pagination/sorting/filtering
- **DB** (`db/`) — SQLAlchemy ORM models (`db/models.py`) and session/engine setup (`db/database.py`), SQLite at `./telemetry.db`

Request/response validation uses Pydantic models defined in `models.py` (separate from SQLAlchemy models in `db/models.py`).

`main.py` is the FastAPI app entry point — it creates tables on startup and registers the readings router.

## API Endpoints

- `POST /readings/` — Ingest a reading, returns calculated CO₂
- `GET /readings/` — Query readings with optional `sensor_id`, `limit`, `offset`, `sort` params
- `GET /readings/{reading_id}` — Fetch single reading by ID
- `GET /health` — Health check

## Key Details

- Database sessions are injected via FastAPI's `Depends(get_db)` in routers
- CO₂ emission factor is hardcoded at 0.233 in `services/readings_service.py`
- No test suite exists yet — pytest is configured but no test files are present
- No Docker, Makefile, or pyproject.toml — dependencies managed via `requirements.txt`
