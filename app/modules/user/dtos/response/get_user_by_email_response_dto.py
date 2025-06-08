from pydantic import BaseModel, EmailStr

class GetUserByEmailResponse(BaseModel):
    full_name: str
    email: EmailStr
    user_name: str
    phone: str

    class Config:
        orm_mode = True  s