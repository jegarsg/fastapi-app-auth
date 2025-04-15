from app.modules.user.dtos.response.get_user_by_email_response_dto import GetUserByEmailResponse
from app.modules.user.repository.user_repository import UserRepository
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

class GetUserByEmailHandler:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def handle(self, email: str) -> GetUserByEmailResponse:
        user = await self.repository.get_by_email(email)
        
        if user:
            user_dict = self.repository.serialize_user(user)  # Serialize user to a dict
            return GetUserByEmailResponse(**user_dict)  # Pass dict to Pydantic model to validate
        else:
            raise HTTPException(status_code=404, detail="User not found")
