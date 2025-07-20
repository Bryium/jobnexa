from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.job import JobCreate, JobOut
from app.services.job_matcher import create_job, get_jobs, get_job_by_id

router = APIRouter()

@router.post("/jobs", response_model=JobOut)
def create(job: JobCreate, db: Session = Depends(get_db)):
    return create_job(db, job)

@router.get("/jobs", response_model=List[JobOut])
def list_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_jobs(db, skip, limit)

@router.get("/jobs/{job_id}", response_model=JobOut)
def read_job(job_id: int, db: Session = Depends(get_db)):
    job = get_job_by_id(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
