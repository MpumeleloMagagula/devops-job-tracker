from pydantic import BaseModel
from datetime import date

# Shared properties for create and read
class JobBase(BaseModel):
    role: str
    company: str
    status: str
    notes: str | None = None
    applied_date: date

# Schema for creating a new job
class JobCreate(JobBase):
    pass

# Schema for returning a job (with ID)
class Job(JobBase):
    id: int

    class Config:
        orm_mode = True  # Allows reading SQLAlchemy objects directly
