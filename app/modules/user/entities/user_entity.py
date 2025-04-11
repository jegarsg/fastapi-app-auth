from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.shared.db_dependency import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    is_active = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    modified_at = Column(DateTime, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False, nullable=False)
    user_name = Column(String, unique=True)
    full_name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    created_by = Column(String)
    modified_by = Column(String)
