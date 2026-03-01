from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.services.user_service import UserService
from app.schemas.user_schema import UserResponse, UserUpdate

router = APIRouter()

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_user(user_id)

@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_all_users()

@router.get("/doctors", response_model=List[UserResponse])
def get_doctors(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_doctors()

@router.get("/patients", response_model=List[UserResponse])
def get_patients(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_patients()

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.update_user(user_id, user_data)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.delete_user(user_id)