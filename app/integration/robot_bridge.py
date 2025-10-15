# app/integration/robot_bridge.py
import asyncio

class RobotBridge:
    def __init__(self):
        self.tasks = []

    async def assign_task(self, robot_id: int, task: str):
        # simulate sending task to robot
        self.tasks.append({"robot_id": robot_id, "task": task})
        print(f"Assigned task '{task}' to robot {robot_id}")
        await asyncio.sleep(0.1)  # simulate async task

    async def get_status(self, robot_id: int):
        # simulate getting robot status
        task = next((t for t in self.tasks if t["robot_id"] == robot_id), None)
        return {"robot_id": robot_id, "task": task["task"] if task else "idle"}
