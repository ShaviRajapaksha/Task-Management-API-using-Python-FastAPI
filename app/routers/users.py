from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app.routers.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if user exists
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    return crud.create_user(db=db, user=user)

@router.get("/me", response_model=schemas.UserResponse)
def read_users_me(current_user = Depends(get_current_user)):
    return current_user