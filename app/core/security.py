"""Security utilities for authentication and authorization"""

import jwt
from datetime import datetime, timedelta
from typing import Optional, List
from passlib.context import CryptContext
from pydantic import BaseModel

from .config import settings


class TokenData(BaseModel):
    """Token data model"""
    username: Optional[str] = None
    roles: List[str] = []


class User(BaseModel):
    """User model for authentication"""
    username: str
    roles: List[str] = []
    disabled: bool = False


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Generate password hash"""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create JWT access token"""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
    return encoded_jwt


def verify_token(token: str) -> Optional[TokenData]:
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        username: str = payload.get("sub")
        roles: List[str] = payload.get("roles", [])
        
        if username is None:
            return None
        
        return TokenData(username=username, roles=roles)
    except jwt.PyJWTError:
        return None


def get_current_active_user(token_data: TokenData) -> User:
    """Get current active user from token data"""
    # In a real application, you would fetch user from database
    # For demo purposes, return a mock user
    return User(
        username=token_data.username,
        roles=token_data.roles,
        disabled=False
    )