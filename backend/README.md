# AI Gen Story Backend

This is the backend for the AI Gen Story project.

## Features
- FastAPI application
- SQLAlchemy models for stories and jobs
- Database setup with SQLite
- API routers for stories and jobs
- Pydantic schemas for request/response validation

## Project structure
- `app/` - application entry points and config
- `db/` - database setup
- `models/` - SQLAlchemy ORM models
- `routers/` - API route definitions
- `schemas/` - request and response validation models

## Run locally

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
2. Start the app:
   ```bash
   uvicorn backend.main:app --reload
   ```

## Notes
This backend is currently set up as a foundation for story generation and job tracking.
