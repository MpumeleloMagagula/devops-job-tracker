# backend/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from .. import schemas, crud

router = APIRouter()

@router.post("/jobs", response_model=schemas.Job)
async def create_job(job: schemas.JobCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_job(db, job)

@router.get("/jobs", response_model=list[schemas.Job])
async def list_jobs(db: AsyncSession = Depends(get_db)):
    return await crud.get_jobs(db)

@router.get("/jobs/{job_id}", response_model=schemas.Job)
async def get_job(job_id: int, db: AsyncSession = Depends(get_db)):
    job = await crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.put("/jobs/{job_id}", response_model=schemas.Job)
async def update_job(job_id: int, updates: schemas.JobUpdate, db: AsyncSession = Depends(get_db)):
    job = await crud.update_job(db, job_id, updates)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.delete("/jobs/{job_id}")
async def delete_job(job_id: int, db: AsyncSession = Depends(get_db)):
    job = await crud.delete_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": f"Job {job_id} deleted."}
