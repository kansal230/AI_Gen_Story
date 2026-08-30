import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from backend.db.database import get_db, SessionLocal
from backend.models.story import Story, StoryNode
from backend.models.job import Job
from backend.schemas.story import CreateStoryRequest, CompleteStoryResponse, StoryRead
from backend.schemas.job import StoryJobResponse


router = APIRouter(prefix="/stories", tags=["stories"])


def get_session_id(session_id: Optional[str] = Cookie(None)):
    if session_id is None:
        session_id = str(uuid.uuid4())
    return session_id


@router.get("/", response_model=list[StoryRead])
async def list_stories(db: Session = Depends(get_db)):
    return db.query(Story).all()


@router.post("/create", response_model=StoryJobResponse, status_code=status.HTTP_201_CREATED)
async def create_story(
    request: CreateStoryRequest,
    background_tasks: BackgroundTasks,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db),
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    job_id = str(uuid.uuid4())

    job = Job(
        job_id=job_id,
        session_id=session_id,
        theme=request.theme,
        status="pending",
    )
    db.add(job)
    db.commit()
    db.refresh(job)

    background_tasks.add_task(generate_story_task, job_id, session_id, request.theme)
    return job


def generate_story_task(job_id: str, session_id: str, theme: str):
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.job_id == job_id).first()
        if not job:
            return

        try:
            job.status = "in_progress"
            db.commit()
            job.status = "completed"
            db.commit()
        except Exception as e:
            job.status = "failed"
            job.error_message = str(e)
            db.commit()
    finally:
        db.close()


@router.get("/{story_id}/complete", response_model=CompleteStoryResponse)
async def complete_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story