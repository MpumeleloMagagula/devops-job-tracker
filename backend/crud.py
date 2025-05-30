# backend/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from . import models, schemas

# Create a job
async def create_job(db: AsyncSession, job: schemas.JobCreate):
    new_job = models.Job(**job.dict())
    db.add(new_job)
    await db.commit()
    await db.refresh(new_job)
    return new_job

# Get all jobs
async def get_jobs(db: AsyncSession):
    result = await db.execute(select(models.Job))
    return result.scalars().all()

# Get a job by ID
async def get_job(db: AsyncSession, job_id: int):
    result = await db.execute(select(models.Job).where(models.Job.id == job_id))
    return result.scalar_one_or_none()

# Update job by ID
async def update_job(db: AsyncSession, job_id: int, updates: schemas.JobUpdate):
    result = await db.execute(select(models.Job).where(models.Job.id == job_id))
    job = result.scalar_one_or_none()
    if job:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(job, field, value)
        await db.commit()
        await db.refresh(job)
    return job

# Delete job by ID
async def delete_job(db: AsyncSession, job_id: int):
    result = await db.execute(select(models.Job).where(models.Job.id == job_id))
    job = result.scalar_one_or_none()
    if job:
        await db.delete(job)
        await db.commit()
    return job
