from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.story import Story
from backend.schemas.story import StoryCreate, StoryRead

router = APIRouter(prefix="/stories", tags=["stories"])


@router.get("/", response_model=list[StoryRead])
async def list_stories(db: Session = Depends(get_db)):
    return db.query(Story).all()


@router.post("/", response_model=StoryRead, status_code=status.HTTP_201_CREATED)
async def create_story(payload: StoryCreate, db: Session = Depends(get_db)):
    story = Story(
        title=payload.title,
        genre=payload.genre,
        summary=payload.summary,
        content=payload.content,
    )
    db.add(story)
    db.commit()
    db.refresh(story)
    return story


@router.get("/{story_id}", response_model=StoryRead)
async def get_story(story_id: int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story
