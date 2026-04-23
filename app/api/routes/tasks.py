from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.tasks import create_task, update_task, get_all_tasks, get_task_by_id, delete_task
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
from app.dependencies import get_current_user
from app.models.user import User

taskrouter = APIRouter(prefix="/tasks", tags=["tasks"])

@taskrouter.post("/", response_model=TaskResponse)
def create_task_(task_data: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, task_data, current_user.id)

@taskrouter.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_tasks(db, current_user.id)

@taskrouter.get("/{task_id}", response_model=TaskResponse)
def get_t(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_task_by_id(db, current_user.id, task_id)

@taskrouter.put("/{task_id}", response_model=TaskResponse)
def updatetask(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_task(db, task_id, task_data, current_user.id)

@taskrouter.delete("/{task_id}")
def deletetask(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_task(db, current_user.id, task_id)