import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.infrastructure.database.base import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_name = Column(String, unique=True)
    full_name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    is_active = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True))
    created_by = Column(String)
    modified_at = Column(DateTime(timezone=True))
    modified_by = Column(String)
    is_deleted = Column(Boolean, nullable=False, default=False)
