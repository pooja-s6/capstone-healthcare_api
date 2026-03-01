from sqlalchemy.orm import Session
from app.models.user import User, UserRole

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: dict):
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_all(self):
        return self.db.query(User).all()

    def get_by_role(self, role: UserRole):
        return self.db.query(User).filter(User.role == role).all()

    def update(self, user_id: int, user_data: dict):
        user = self.get_by_id(user_id)
        if user:
            for key, value in user_data.items():
                if value is not None:
                    setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user

    def delete(self, user_id: int):
        user = self.get_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user