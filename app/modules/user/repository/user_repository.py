from sqlalchemy.future import select
from app.infrastructure.database.models.user_model import User
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    def serialize_user(self, user: User) -> dict:
        return {
            "full_name": user.full_name,
            "email": user.email,
            "user_name": user.user_name,
            "phone": user.phone
        }


    async def get_by_phone(self, phone: str):
        result = await self.db.execute(select(User).where(User.phone == phone))
        return result.scalars().first()

    async def create(self, user: User):
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

