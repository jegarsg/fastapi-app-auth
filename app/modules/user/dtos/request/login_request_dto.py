from pydantic import BaseModel, EmailStr, Field

class LoginUserDTO(BaseModel):
    email: EmailStr
    password: str
