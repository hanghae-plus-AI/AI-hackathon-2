from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base


class ResultEntity(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String)
    url = Column(String)
    title = Column(String)
    summary = Column(String)
    thumbnail = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
