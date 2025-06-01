# backend/tests/test_jobs.py

import pytest
from httpx import AsyncClient
from backend.main import app
from backend.db.session import get_db
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from backend.models import Base
from backend.app.api.routes import app 
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db 

#from crud import app 

# Use a separate test database
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Create test DB engine and session
test_engine = create_async_engine(TEST_DATABASE_URL, future=True)
TestSessionLocal = sessionmaker(bind=test_engine, class_=AsyncSession, expire_on_commit=False)

# Override the DB dependency
async def override_get_db():
    async with TestSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

# Setup DB for testing
@pytest.fixture(scope="module", autouse=True)
async def setup_db():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_create_job():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/jobs", json={"company": "OpenAI", "position": "DevOps", "notes": "Cool role"})
        assert response.status_code == 200
        assert response.json()["company"] == "OpenAI"

@pytest.mark.asyncio
async def test_list_jobs():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/jobs")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_update_job():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.put("/jobs/1", json={"status": "Interviewing"})
        assert response.status_code == 200
        assert response.json()["status"] == "Interviewing"

@pytest.mark.asyncio
async def test_delete_job():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.delete("/jobs/1")
        assert response.status_code == 200
        assert "deleted" in response.json()["message"].lower()
