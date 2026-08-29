from pydantic import BaseModel, Field
from typing import Optional


class JobCreate(BaseModel):
    title: str = Field(..., min_length=1)
    status: Optional[str] = "pending"
    prompt: str = Field(..., min_length=1)
    result: Optional[str] = None


class JobRead(BaseModel):
    id: int
    title: str
    status: str
    prompt: str
    result: Optional[str] = None

    class Config:
        from_attributes = True
