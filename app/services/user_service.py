from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.models.user import UserRole

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def get_user_by_id(self, user_id: int):
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def get_all_users(self):
        return self.user_repo.get_all()

    def get_doctors(self):
        return self.user_repo.get_by_role(UserRole.doctor)

    def get_patients(self):
        return self.user_repo.get_by_role(UserRole.patient)

    def update_user(self, user_id: int, user_data: dict):
        user = self.user_repo.update(user_id, user_data)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def delete_user(self, user_id: int):
        user = self.user_repo.delete(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user