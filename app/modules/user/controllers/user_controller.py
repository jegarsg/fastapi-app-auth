from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.db_dependency import get_db
from app.modules.user.commands.handlers.register_user_handler import RegisterUserHandler
from app.modules.user.dtos.user_dto import RegisterUserDTO

# Mount this under /api/user in main.py
router = APIRouter(prefix="/api/user", tags=["User"])

@router.post("/register")
async def register_user(
    payload: RegisterUserDTO,
    db: AsyncSession = Depends(get_db),
):
    handler = RegisterUserHandler(db)
    user = await handler.handle(payload)
    return user
