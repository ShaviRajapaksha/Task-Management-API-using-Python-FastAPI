from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database
from app.routers.auth import get_current_user

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    return crud.create_category(db=db, category=category, user_id=current_user.id)

@router.get("/", response_model=List[schemas.CategoryResponse])
def read_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    categories = crud.get_categories(db, user_id=current_user.id, skip=skip, limit=limit)
    return categories

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    if not crud.delete_category(db, category_id=category_id, user_id=current_user.id):
        raise HTTPException(status_code=404, detail="Category not found")
    return None