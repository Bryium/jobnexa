from pydantic import BaseModel
from typing import List

class RoadmapBase(BaseModel):
    job_id: int
    steps: List[str]

class RoadmapCreate(RoadmapBase):
    pass

class RoadmapOut(RoadmapBase):
    id: int

    class Config:
        from_attributes = True
