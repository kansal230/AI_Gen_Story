# AI Gen Story

This project contains the backend for an AI-powered story generation application built with FastAPI, SQLAlchemy, and Pydantic.

## Features
- FastAPI app with CORS enabled
- SQLite database setup
- SQLAlchemy models for stories and jobs
- API routes for story and job operations
- Request/response validation with Pydantic schemas
- Environment-based configuration via `.env`

## Project structure

```text
AI_Gen_Story/
├── backend/
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── job.py
│   │   └── story.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── job.py
│   │   └── story.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── job.py
│   │   └── story.py
│   ├── main.py
│   └── README.md
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env` if needed.

## Run locally

From the project root, run:

```bash
cd backend
python main.py
```

Then open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## Notes

This backend is currently set up as the foundation for story generation and background job tracking. It can be extended with AI generation services, authentication, and richer story workflows.
