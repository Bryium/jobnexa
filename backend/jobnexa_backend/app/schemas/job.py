from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    title: str
    description: str
    industry: str
    experience_level: str

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    id: int
    posted_at: datetime

    class Config:
        orm_mode = True
