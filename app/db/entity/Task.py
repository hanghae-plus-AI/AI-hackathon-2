from db import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime


class TaskEntity(Base):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
