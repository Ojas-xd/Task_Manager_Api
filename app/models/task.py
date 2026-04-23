from sqlalchemy import Integer,Column,String,ForeignKey,DateTime,Enum
from sqlalchemy.sql import func
from app.database import Base
import enum

class TaskStatus(str,enum.Enum):
    pending="pending"
    in_progress="in_progress"
    completed="completed"
    
class Task(Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String,nullable=False)
    description=Column(String,nullable=True)
    status=Column(Enum(TaskStatus),default=TaskStatus.pending)
    deadline=Column(DateTime,nullable=True)
    owner_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    assigned_to=Column(Integer,ForeignKey("users.id"),nullable=True)
    created_at=Column(DateTime,default=func.now())