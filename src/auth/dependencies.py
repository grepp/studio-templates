"""
FastAPI 의존성 주입 — 인증/인가 미들웨어.
라우터에서 `Depends(get_current_user)` 형태로 사용합니다.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.auth.jwt import verify_token
from src.logger import get_logger

logger = get_logger(__name__)
bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict:
    """유효한 Access Token을 검증하고 페이로드를 반환합니다."""
    payload = verify_token(credentials.credentials, expected_type="access")
    if not payload:
        logger.warning("invalid_token_attempt")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="인증 토큰이 유효하지 않습니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload


def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    """관리자 권한을 요구합니다."""
    if current_user.get("role") != "admin":
        logger.warning("unauthorized_admin_access", user=current_user.get("sub"))
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="관리자 권한이 필요합니다.",
        )
    return current_user
