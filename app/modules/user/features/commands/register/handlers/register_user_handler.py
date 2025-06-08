import re
from app.shared.utils.encryption import hash_password
from app.shared.utils.string_generator import generate_username
from app.modules.user.features.commands.register.register_user_command import RegisterUserCommand
from app.infrastructure.database.models.user_model import User
from app.modules.user.repository.user_repository import UserRepository


class RegisterUserHandler:
    def __init__(self, db):
        self.repo = UserRepository(db)

    async def handle(self, command: RegisterUserCommand):
        # Validate phone number format
        if not re.match(r"^\d{10,12}$", command.phone):
            raise ValueError("Phone number must be 10-12 digits")

        # Normalize phone number
        command.phone = command.phone if command.phone.startswith("+62") else f"+62{command.phone}"

        # Check for existing email or phone
        if await self.repo.get_by_email(command.email):
            raise ValueError("Email already registered")

        if await self.repo.get_by_phone(command.phone):
            raise ValueError("Phone already registered")

        # Hash password and generate username
        hashed_password = hash_password(command.password)
        username = generate_username(command.full_name)

        # Create new user object
        user = User(
            full_name=command.full_name,
            user_name=username,
            email=command.email,
            phone=command.phone,
            password=hashed_password,
        )

        # Save to database
        return await self.repo.create(user)