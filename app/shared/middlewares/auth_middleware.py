from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from jose import jwt, JWTError
from app.core.config import get_settings

settings = get_settings()

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if token and token.startswith("Bearer "):
            token = token[7:]
            try:
                payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
                request.state.user = {
                    "email": payload.get("sub"),
                    "exp": payload.get("exp"),
                    "role": payload.get("role", None)  # or other custom claims
                }
            except JWTError:
                request.state.user = None
        else:
            request.state.user = None

        response = await call_next(request)
        return response
