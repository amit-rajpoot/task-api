from pydantic import BaseModel, ConfigDict , EmailStr
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description:Optional[str] = None
    priority:Optional[str] = "LOW"
    due_date:Optional[datetime] = None

class TaskCreate(TaskBase):
    pass 

class TaskUpdate(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    completed:Optional[bool] = None
    priority:Optional[str] = None
    due_date:Optional[datetime] = None

class TaskOut(TaskBase):
    id:int
    completed:bool
    owner_id:int
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)