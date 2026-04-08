"""
JWT Access / Refresh 토큰 발급 및 검증.
"""
from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt

from src.config import get_settings

settings = get_settings()


def create_access_token(subject: str, role: str = "user") -> str:
    payload = {
        "sub": subject,
        "role": role,
        "type": "access",
        "exp": datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        "iat": datetime.now(UTC),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_refresh_token(subject: str) -> str:
    payload = {
        "sub": subject,
        "type": "refresh",
        "exp": datetime.now(UTC) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        "iat": datetime.now(UTC),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str) -> dict:
    """
    토큰 디코딩. 만료 또는 무결성 오류 시 JWTError 발생.
    로그에 토큰 값을 출력하지 마세요.
    """
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])


def verify_token(token: str, expected_type: str = "access") -> dict | None:
    try:
        payload = decode_token(token)
        if payload.get("type") != expected_type:
            return None
        return payload
    except JWTError:
        return None
