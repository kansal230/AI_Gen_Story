import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from backend.core.config import settings
except ModuleNotFoundError:
    from core.config import settings

try:
    from backend.db.database import create_tables
    from backend.routers.story import router as story_router
    from backend.routers.job import router as job_router
except ModuleNotFoundError:
    from db.database import create_tables
    from routers.story import router as story_router
    from routers.job import router as job_router

app = FastAPI(
    title="Choose your own Adventure game API",
    description="Api to generate cool stories",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story_router, prefix=settings.api_prefix, tags=["stories"])
app.include_router(job_router, prefix=settings.api_prefix, tags=["jobs"])

# Both model modules are imported via the routers above, so every table is
# registered on Base.metadata by the time this runs.
create_tables()


@app.get("/")
async def root():
    return {"message": "AI Gen Story backend is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)