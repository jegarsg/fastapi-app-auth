from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class RegisterUserValidator(BaseModel):
    full_name: str
    password: str
    email: EmailStr
    phone: str

    @validator('full_name')
    def validate_full_name(cls, v):
        if len(v.strip()) < 3:
            raise ValueError("Full name must be at least 3 characters long")
        return v

    @validator('phone')
    def validate_phone(cls, v):
        if not v.isdigit():
            raise ValueError("Phone number must only contain digits")
        if not (10 <= len(v) <= 12):
            raise ValueError("Phone number must be between 10 and 12 digits")
        return v
