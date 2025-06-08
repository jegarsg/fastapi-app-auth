from fastapi import FastAPI
from app.modules.user.controllers.user_controller import router as user_router
from app.infrastructure.database.session import engine
from app.infrastructure.database.base import Base
from app.core.config import get_settings
from app.infrastructure.database.models import user_model  # ensure model import
from app.shared.middlewares.auth_middleware import AuthMiddleware


settings = get_settings()
print("✅ DATABASE_URL from env:", settings.DATABASE_URL)

app = FastAPI()
app.add_middleware(AuthMiddleware)

# ✅ Run table creation in async-safe way
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tables created")

# Register routes
app.include_router(user_router)
