from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models
from app.database import get_db
from app.services.utils import get_current_user
from app.schemas.roadmap import RoadmapCreate, RoadmapOut

router = APIRouter()

@router.post("/save", response_model=RoadmapOut)
def save_roadmap(roadmap: RoadmapCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_roadmap = models.Roadmap(
        job_id=roadmap.job_id,
        steps=roadmap.steps,
        user_id=user.id
    )
    db.add(new_roadmap)
    db.commit()
    db.refresh(new_roadmap)
    return new_roadmap

@router.get("/", response_model=List[RoadmapOut])
def get_user_roadmaps(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Roadmap).filter(models.Roadmap.user_id == user.id).all()
