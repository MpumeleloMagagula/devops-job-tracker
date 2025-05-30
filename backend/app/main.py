from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas, crud
from .database import engine, Base, get_db
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# FastAPI instance
app = FastAPI()

# Auto-create tables at startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Register Prometheus instrumentator
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

@app.get("/")
def root():
    return {"message": "DevOps Job Tracker API is live!"}

# Create job endpoint
@app.post("/jobs/", response_model=schemas.Job)
async def create_job(job: schemas.JobCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_job(db, job)

# List all jobs
@app.get("/jobs/", response_model=list[schemas.Job])
async def list_jobs(db: AsyncSession = Depends(get_db)):
    return await crud.get_jobs(db)

# Get job by ID
@app.get("/jobs/{job_id}", response_model=schemas.Job)
async def read_job(job_id: int, db: AsyncSession = Depends(get_db)):
    job = await crud.get_job(db, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

# Delete job by ID
@app.delete("/jobs/{job_id}", response_model=schemas.Job)
async def delete_job(job_id: int, db: AsyncSession = Depends(get_db)):
    job = await crud.delete_job(db, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
