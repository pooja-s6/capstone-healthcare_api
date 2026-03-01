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
def get_all_patients(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    return user_service.get_patients()

@router.get("/{patient_id}", response_model=UserResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    return user_service.get_user_by_id(patient_id)

@router.put("/{patient_id}", response_model=UserResponse)
def update_patient(patient_id: int, patient_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    return user_service.update_user(patient_id, patient_data.model_dump(exclude_unset=True))

@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_service = UserService(db)
    user_service.delete_user(patient_id)