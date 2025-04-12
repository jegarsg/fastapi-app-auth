from pydantic import BaseModel, EmailStr, Field

class GetUserByEmailResponse(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    phone: str
    createdby:str