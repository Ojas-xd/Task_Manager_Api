from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    deadline: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    deadline: Optional[datetime] = None
    owner_id: int
    assigned_to: Optional[int] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)