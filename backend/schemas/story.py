from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime


class StoryOptionsSchema(BaseModel):
    text: str
    node_id: Optional[int] = None


class StoryNodeBase(BaseModel):
    is_ending: bool = False
    is_winning_ending: bool = False
    content: str


class CompleteStoryNodeResponse(StoryNodeBase):
    id: int
    options: List[StoryOptionsSchema] = []

    class Config:
        from_attributes = True


class StoryBase(BaseModel):
    title: str
    session_id: Optional[str] = None

    class Config:
        from_attributes = True


class CreateStoryRequest(StoryBase):
    theme: str


class StoryRead(BaseModel):
    id: int
    title: str
    genre: Optional[str] = None
    summary: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_node_id: Optional[CompleteStoryNodeResponse] = None
    all_nodes: Dict[int, CompleteStoryNodeResponse] = {}

    class Config:
        from_attributes = True


StoryCreate = CreateStoryRequest
StoryReadAlias = StoryRead