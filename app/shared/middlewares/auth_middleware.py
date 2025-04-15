from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from jose import jwt, JWTError
from app.core.config import get_settings
from datetime import datetime

settings = get_settings()

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        
        if token and token.startswith("Bearer "):
            token = token[7:]  # Extract the token (after "Bearer ")
            
            try:
                # Decode the JWT and extract the claims
                payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
                email = payload.get("sub")
                exp = payload.get("exp")
                
                if exp and datetime.utcfromtimestamp(exp) < datetime.utcnow():
                    raise JWTError("Token is expired")  # Token expiration check

                # Store the claims in the request state
                request.state.user = {
                    "email": email,
                    "exp": exp,
                    "role": payload.get("role", None)  # or other custom claims
                }
            except JWTError as e:
                request.state.user = None
                print(f"JWT error: {e}")  # Log JWT errors for debugging
        else:
            request.state.user = None

        # Proceed with the request
        response = await call_next(request)
        return response
