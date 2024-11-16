from typing import List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db import get_db
from sqlalchemy.orm import Session
from db.entity.Task import TaskEntity
from db.entity.Result import ResultEntity
from ai import tredi

task_router = APIRouter(prefix="/keyword")
tasks_router = APIRouter(prefix="/keywords")


class TaskRequest(BaseModel):
    taskId: int
    keyword: str


class TasksRequest(BaseModel):
    taskId: int
    keywords: List[str]


# 검색 단건 요청
@task_router.post("")
async def task(request: TaskRequest, session: Session = Depends(get_db)):
    print(request)
    task: TaskEntity = (
        session.query(TaskEntity).filter(TaskEntity.task_id == request.taskId).first()
    )

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    result = tredi.run(request.keyword)

    task.status = "COMPLETE"

    result_entity = ResultEntity(
        task_id=task.task_id,
        url=result["link"],
        title=result["title"],
        summary=result["summary"],
        thumbnail="abc",
    )

    session.add(result_entity)
    session.commit()

    return result


# 검색 다건 요청
@tasks_router.post("")
async def tasks(request: TasksRequest, session: Session = Depends(get_db)):

    task = session.query(TaskEntity).filter(TaskEntity.taskId == request.taskId).first()

    # model 실행
    # request.keywords 와 조합하여 Model을 실행


# @task_router.get("/{taskId}")
# async def task(taskId: str, session: Session = Depends(get_db)):
#     task = session.query(TaskEntity).filter(TaskEntity.taskId == taskId).first()

#     if task is None:
#         raise HTTPException(status_code=404, detail="Task not found")

#     return task
