from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.user.dtos.request.login_request_dto import LoginUserDTO
from app.modules.user.repository.user_repository import UserRepository
from app.shared.utils.encryption import verify_password
from app.shared.utils.jwt import create_access_token
from fastapi import HTTPException, status

class LoginUserHandler:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def handle(self, payload: LoginUserDTO):
        user = await self.repo.get_by_email(payload.email)
        if not user or not verify_password(payload.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        token = create_access_token(data={"sub": user.email})
        return {"access_token": token, "token_type": "bearer"}
