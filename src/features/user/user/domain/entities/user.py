from sqlalchemy import Column, String, Date, Boolean

from core.models.base_model_audit import BaseAuditModel
from config.base import Base


class User(BaseAuditModel):
    __tablename__ = 'users'
    
    nickname = Column(String(20), nullable=False)
    password = Column(String, nullable=False)
    lastAuth = Column(Date, nullable=True)
    origin = Column(String(20), nullable=True)
    active = Column(Boolean, nullable=False)
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "nickname": self.nickname,
            "lastAuth": self.lastAuth,
            "origin": self.origin,
            "active": self.active,
        }