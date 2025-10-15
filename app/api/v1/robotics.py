# app/api/v1/robotics.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.db.session import get_db
from app.services.robotics_service import RoboticsService

router = APIRouter()

class TaskRequest(BaseModel):
    robot_id: int
    task: str

@router.post("/task")
async def assign_task(req: TaskRequest, db: AsyncSession = Depends(get_db)):
    return await RoboticsService.assign_task(db, req.robot_id, req.task)
