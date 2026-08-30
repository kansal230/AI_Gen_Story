import uuid
from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from backend.db.database import get_db, SessionLocal
from backend.models.story import Story, StoryNode
from backend.schemas.story import StoryCreate, StoryRead
from backend.models.job import StoryJob
from backend.schemas.story import ( CompleteStoryNodeResponse, CreateStoryRequest)
from backend.schemas.job import StoryJobCreate, StoryJobResponse


router = APIRouter(prefix="/stories", tags=["stories"])
#backend URL/api/stories/create-story

def get_session_id(session_id: Optional[str] = Cookie(None)):
    if session_id not in session_id:
        session_id = str(uuid.uuid4())
    return session_id

@router.get("/", response_model=list[StoryRead])
async def list_stories(db: Session = Depends(get_db)):
    return db.query(Story).all()


@router.post("/create", response_model=StoryjobResponse, status_code=status.HTTP_201_CREATED)
async def create_story(request: CreateStoryRequest, background_tasks: BackgroundTasks,
response: Response, session_id: str = Depends(get_session_id),
 db: Session = Depends(get_db)):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    job_id = str(uuid.uuid4())

    job = StoryJob(
        id=job_id,
        session_id=session_id,
        theme=request.theme,
        status=r"pending"
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

def generate_story(job_id: str, session_id: str, theme: str, db: Session):
    try:
        # Simulate story generation process
        # Here you would implement the actual story generation logic
        # For demonstration, we will just create a dummy story
        story = Story(
            title=f"Story based on theme: {theme}",
            session_id=session_id,
            root_node_id=1  # Assuming the root node ID is 1 for simplicity
        )
        db.add(story)
        db.commit()
        db.refresh(story)

        # Update job status to completed
        job = db.query(StoryJob).filter(StoryJob.id == job_id).first()
        if job:
            job.status = "completed"
            job.story_id = story.id
            db.commit()
    except Exception as e:
        # Update job status to failed in case of an error
        job = db.query(StoryJob).filter(StoryJob.id == job_id).first()
        if job:
            job.status = "failed"
            job.error_message = str(e)
            db.commit()

@router.get("/{story_id}", response_model=StoryRead)
async def get_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story
