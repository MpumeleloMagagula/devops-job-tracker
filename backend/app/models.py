from sqlalchemy import Column, Integer, String, Date
from .database import Base

# SQLAlchemy model representing a job application
class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, index=True)
    company = Column(String, index=True)
    status = Column(String)  # e.g., Applied, Interviewing
    notes = Column(String)   # Interview notes or feedback
    applied_date = Column(Date)  # Date application was submitted
