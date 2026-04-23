from app.models.task import Task, TaskStatus
from app.schemas.tasks import TaskCreate, TaskUpdate
from fastapi import HTTPException


def create_task(db, task_data: TaskCreate, current_user_id: int):
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        deadline=task_data.deadline,
        status=TaskStatus.pending,
        owner_id=current_user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks(db,current_user_id):
    a=db.query(Task).filter(Task.owner_id==current_user_id).all()
    return a

def get_task_by_id(db,current_user_id,task_id:int):
    a=db.query(Task).filter(Task.id==task_id).first()
    if a is None:
        raise HTTPException(status_code=404,detail="Task not found")
    if a.owner_id!=current_user_id:
        raise HTTPException(status_code=403,detail="Not authorized")
    return a

def update_task(db,task_id:int,task_data:TaskUpdate, current_user_id:int):
    a=get_task_by_id(db,current_user_id,task_id)
    if task_data.title is not None:
        a.title = task_data.title
    if task_data.status is not None:
        a.status = task_data.status
    if task_data.description is not None:
        a.description=task_data.description
    if task_data.deadline is not None:
        a.deadline=task_data.deadline
    db.commit()
    db.refresh(a)
    return a

def delete_task(db,current_user_id,task_id:int):
    a=get_task_by_id(db,current_user_id,task_id)
    db.delete(a)
    db.commit()
    return {"message":"Task deleted successfully"}
    
    
