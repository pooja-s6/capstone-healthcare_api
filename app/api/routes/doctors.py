from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.services.user_service import UserService
from app.schemas.user_schema import UserResponse, UserUpdate
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
def get_all_doctors(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    return user_service.get_doctors()

@router.get("/{doctor_id}", response_model=UserResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    return user_service.get_user_by_id(doctor_id)

@router.put("/{doctor_id}", response_model=UserResponse)
def update_doctor(doctor_id: int, doctor_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    return user_service.update_user(doctor_id, doctor_data.model_dump(exclude_unset=True))

@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    user_service.delete_user(doctor_id)