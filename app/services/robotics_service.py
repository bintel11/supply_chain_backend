# app/services/robotics_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models_tracking import Robot

class RoboticsService:

    @staticmethod
    async def assign_task(db: AsyncSession, robot_id: int, task: str):
        result = await db.execute(select(Robot).where(Robot.id == robot_id))
        robot = result.scalar_one()
        robot.task = task
        await db.commit()
        await db.refresh(robot)
        return robot
