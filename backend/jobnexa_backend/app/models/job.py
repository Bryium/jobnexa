from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    industry = Column(String)
    experience_level = Column(String)
    posted_at = Column(DateTime, default=datetime.utcnow)

    roadmap = relationship("Roadmap", back_populates="job", uselist=False)
