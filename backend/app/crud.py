from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession 
from app import models, schemas

# Create a job record
async def create_job(db: AsyncSession, job: schemas.JobCreate):
    new_job = models.JobApplication(**job.dict())
    db.add(new_job)
    await db.commit()
    await db.refresh(new_job)
    return new_job

# Get all jobs
async def get_jobs(db: AsyncSession):
    result = await db.execute(select(models.JobApplication))
    return result.scalars().all()

# Get a single job by ID
async def get_job(db: AsyncSession, job_id: int):
    result = await db.execute(select(models.JobApplication).where(models.JobApplication.id == job_id))
    return result.scalar_one_or_none()

# Delete a job by ID
async def delete_job(db: AsyncSession, job_id: int):
    job = await get_job(db, job_id)
    if job:
        await db.delete(job)
        await db.commit()
    return job
