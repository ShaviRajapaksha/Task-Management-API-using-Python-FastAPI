from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from app import schemas, crud, database
from app.routers.auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    # Check if category exists if provided
    if task.category_id:
        category = crud.get_categories(db, current_user.id, limit=1)
        if not any(c.id == task.category_id for c in category):
            raise HTTPException(status_code=404, detail="Category not found")
    
    return crud.create_task(db=db, task=task, user_id=current_user.id)

@router.get("/", response_model=List[schemas.TaskResponse])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = Query(None, regex="^(pending|in_progress|completed)$"),
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    tasks = crud.get_tasks(db, user_id=current_user.id, skip=skip, limit=limit, status=status)
    return tasks

@router.get("/{task_id}", response_model=schemas.TaskResponse)
def read_task(
    task_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    task = crud.get_task(db, task_id=task_id, user_id=current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    task = crud.update_task(db, task_id=task_id, user_id=current_user.id, task_update=task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    if not crud.delete_task(db, task_id=task_id, user_id=current_user.id):
        raise HTTPException(status_code=404, detail="Task not found")
    return None