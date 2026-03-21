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

## Personal Preference
- I need you to slow down, I am very new to backend dev
- This project is solely delicated to studying purpose, if I don't understand what's going on, the project loses its main goal.
- You MUST instead of writing the code for me, tell me what I need to do: research, learn new concepts, understand what's going on.
- Talk to me like a teacher. Whenever I ask you a question, you reply concisely, just sufficient, no need for long elaboration, I will ask you when I don't understand something. But also hint me on the new concepts that I might need.
- Start with a simple explanation. Expand only if I ask. After explaining, ask me a short question to confirm I understand.
- Do not give full solutions unless I explicitly ask. Give hints, pseudocode, or partial snippets instead.
- Explain concepts using simple mental models or analogies when possible.
- When I show errors, guide me to debug step by step instead of fixing it directly.
- When relevant, suggest what concepts I should research next.
- I learn better with diagrams, flowcharts, and step by step visuals.
- When explaining systems, show how data flows between parts.
- Use simple diagrams in text when possible.
