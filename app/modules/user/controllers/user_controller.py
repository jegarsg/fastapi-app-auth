from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared.db_dependency import get_db
from app.modules.user.features.commands.register.handlers.register_user_handler import RegisterUserHandler
from app.modules.user.dtos.request.user_request_dto import RegisterUserDTO
from app.modules.user.features.commands.login.handlers.login_handler import LoginUserHandler
from app.modules.user.dtos.request.login_request_dto import LoginUserDTO
from app.modules.user.features.queries.get_user_by_email.handlers.get_user_by_email_handler import GetUserByEmailHandler
from app.shared.utils.jwt import get_email_from_token
from app.modules.user.dtos.user_dto import UserOutDto

# Mount this under /api/user in main.py
router = APIRouter(prefix="/api", tags=["User"])

@router.post("/user/register")
async def register_user(
    payload: RegisterUserDTO,
    db: AsyncSession = Depends(get_db),
):
    handler = RegisterUserHandler(db)
    user = await handler.handle(payload)
    return user


@router.post("/secure/login")
async def login(payload: LoginUserDTO, db: AsyncSession = Depends(get_db)):
    handler = LoginUserHandler(db)
    return await handler.handle(payload)



@router.post("/user/secure/get-by-email", response_model=UserOutDto)
async def get_user_by_email(
    db: AsyncSession = Depends(get_db),
    email: str = Depends(get_email_from_token),
):
    handler = GetUserByEmailHandler(db)
    user = await handler.handle(email)
    return user