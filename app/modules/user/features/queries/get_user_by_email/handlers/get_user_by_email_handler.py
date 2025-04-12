# app/modules/user/queries/handlers/get_user_by_email_handler.py
from app.modules.user.repository.user_repository import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.user.dtos.response.get_user_by_email_response_dto import GetUserByEmailResponse

class GetUserByEmailHandler:
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def handle(self, email: str) -> GetUserByEmailResponse:
        user = await self.repository.get_by_email(email)
        return GetUserByEmailResponse.model_validate(user)
