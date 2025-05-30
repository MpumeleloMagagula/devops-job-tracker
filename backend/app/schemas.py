from pydantic import BaseModel
from typing import Optional
from datetime import date

# Shared properties for create and read
class JobBase(BaseModel):
    role: str
    company: str
    status: str = "Applied" # default
    position: str
    notes: Optional[str] = None
    applied_date: date

# Schema for creating a new job
class JobCreate(JobBase):
    pass

# Used when updating a job
class JobUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None

# Schema for returning a job (with ID)
class Job(JobBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Allows reading SQLAlchemy objects directly
