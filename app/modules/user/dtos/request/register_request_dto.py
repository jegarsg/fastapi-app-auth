from pydantic import BaseModel, EmailStr, Field

class UserRegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str

class UserResponse(BaseModel):
    user_id: str
    user_name: str
    email: str
    phone: str
