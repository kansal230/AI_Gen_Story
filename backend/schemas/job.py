from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class StoryJobBase(BaseModel):
    theme: str


class StoryJobResponse(BaseModel):
    job_id: str
    status: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    story_id: Optional[int] = None
    error_message: Optional[str] = None

    class Config:
        from_attributes = True

class StoryJobCreate(StoryJobBase):
    pass

class CreateStoryJobRequest(StoryJobBase):
    pass

# Backward-compatible aliases for older imports
JobCreate = StoryJobCreate
JobRead = StoryJobResponse