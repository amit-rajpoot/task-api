
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.model import Task
from app.core.deps import get_current_user
from app.schemas.tasks import TaskCreate, TaskOut, TaskUpdate


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# =========================
# CREATE TASK
# =========================

@router.post(
    "/",
    response_model=TaskOut,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_in: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    new_task = Task(
        title=task_in.title,
        description=task_in.description,
        priority=task_in.priority,
        owner_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# =========================
# GET ALL MY TASKS
# =========================

@router.get(
    "/",
    response_model=List[TaskOut]
)
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    tasks = (
        db.query(Task)
        .filter(Task.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return tasks


# =========================
# GET SINGLE TASK
# =========================

@router.get(
    "/{task_id}",
    response_model=TaskOut
)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == current_user.id
        )
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


# =========================
# UPDATE TASK
# =========================

@router.put(
    "/{task_id}",
    response_model=TaskOut
)
def update_task(
    task_id: int,
    task_in: TaskUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == current_user.id
        )
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Update only fields provided by user

    if task_in.title is not None:
        task.title = task_in.title

    if task_in.description is not None:
        task.description = task_in.description

    if task_in.priority is not None:
        task.priority = task_in.priority

    if task_in.completed is not None:
        task.completed = task_in.completed

    db.commit()
    db.refresh(task)

    return task


# =========================
# DELETE TASK
# =========================

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == current_user.id
        )
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return

