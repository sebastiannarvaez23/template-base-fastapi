import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    first_last_name = Column(String, nullable=False)
    second_last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String(10), nullable=False)
    birth_date = Column(String, nullable=False)
    avatar = Column(String, nullable=True) 