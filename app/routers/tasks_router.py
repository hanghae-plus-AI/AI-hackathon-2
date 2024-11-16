from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from db import get_db
from sqlalchemy.orm import Session
from db.entity.Task import TaskEntity
from requests import HTTPException

task_router = APIRouter(prefix="/tasks")


class TasksRequest(BaseModel):
    taskId: str
    keywords: List[str]


@task_router.post("")
async def task(request: TasksRequest, session: Session = Depends(get_db)):

    try:
        task = (
            session.query(TaskEntity)
            .filter(TaskEntity.taskId == request.taskId)
            .first()
        )
        # request.keywords 와 조합하여 Model을 실행

    except:
        raise HTTPException(status_code=404, detail="Task not found")


# @task_router.get("/{taskId}")
# async def task(taskId: str, session: Session = Depends(get_db)):
#     task = session.query(TaskEntity).filter(TaskEntity.taskId == taskId).first()

#     if task is None:
#         raise HTTPException(status_code=404, detail="Task not found")

#     return task
