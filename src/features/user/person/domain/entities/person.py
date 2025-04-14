from sqlalchemy import Column, String, Date

from core.models.base_model_audit import BaseAuditModel
from src.config.base import Base


class Person(BaseAuditModel):
    __tablename__ = 'persons'

    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=True)
    first_last_name = Column(String, nullable=False)
    second_last_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    avatar = Column(String, nullable=True)
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "second_name": self.second_name,
            "first_last_name": self.first_last_name,
            "second_last_name": self.second_last_name,
            "email": self.email,
            "phone": self.phone,
            "birth_date": self.birth_date,
            "avatar": self.avatar,
        }