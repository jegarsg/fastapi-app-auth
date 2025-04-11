from pydantic import BaseModel, EmailStr, Field

class RegisterUserDTO(BaseModel):
    full_name: str
    password: str
    email: EmailStr
    phone: str