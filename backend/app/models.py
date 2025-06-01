from sqlalchemy import Column, Integer, String, Date
from .database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import declarative_base



Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    status = Column(String(50), default="Applied")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# SQLAlchemy model representing a job application
class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, index=True)
    company = Column(String, index=True)
    status = Column(String)  # e.g., Applied, Interviewing
    notes = Column(String)   # Interview notes or feedback
    applied_date = Column(Date)  # Date application was submitted
