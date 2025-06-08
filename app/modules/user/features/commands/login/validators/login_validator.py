from pydantic import BaseModel, EmailStr, Field

class LoginUserValidator(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., min_length=6, example="strongpassword123")
