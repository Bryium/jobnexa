from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from datetime import datetime

from app.models.job import Job
from app.schemas.job import JobCreate


def create_job(db: Session, job: JobCreate, user_id: int = None) -> Job:
    """
    Create a new job entry.
    """
    try:
        job_data = job.dict()
        if user_id is not None:
            job_data["user_id"] = user_id 
        job_data["posted_at"] = datetime.utcnow()
        db_job = Job(**job_data)

        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError("Database error during job creation.") from e


def get_jobs(db: Session, skip: int = 0, limit: int = 10) -> List[Job]:
    """
    Retrieve all jobs with pagination.
    """
    return db.query(Job).offset(skip).limit(limit).all()


def get_job_by_id(db: Session, job_id: int) -> Optional[Job]:
    """
    Retrieve a single job by its ID.
    """
    return db.query(Job).filter(Job.id == job_id).first()
