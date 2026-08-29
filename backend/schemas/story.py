from pydantic import BaseModel, Field
from typing import Optional


class StoryCreate(BaseModel):
    title: str = Field(..., min_length=1)
    genre: Optional[str] = None
    summary: Optional[str] = None
    content: str = Field(..., min_length=1)


class StoryRead(BaseModel):
    id: int
    title: str
    genre: Optional[str] = None
    summary: Optional[str] = None
    content: str

    class Config:
        from_attributes = True
