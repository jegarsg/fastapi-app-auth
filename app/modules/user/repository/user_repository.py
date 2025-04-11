from sqlalchemy.future import select
from app.infrastructure.database.models.user_model import User
from typing import Optional

class UserRepository:

    def __init__(self, db):
        self.db = db

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalars().first()



    async def get_by_phone(self, phone: str):
        result = await self.db.execute(select(User).where(User.phone == phone))
        return result.scalars().first()

    async def create(self, user: User):
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

