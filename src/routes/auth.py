"""
인증 API 라우터 — 로그인 / 토큰 갱신.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.jwt import create_access_token, create_refresh_token, verify_token
from src.db.session import get_db
from src.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str  # 로그에 절대 출력하지 마세요


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str


@router.post("/login", response_model=TokenResponse, summary="로그인")
async def login(
    body: LoginRequest,
    db: AsyncSession = Depends(get_db),
) -> TokenResponse:
    """
    이메일/비밀번호로 로그인하여 JWT 토큰을 발급합니다.
    TODO: 실제 DB 사용자 조회 및 비밀번호 검증 로직을 구현하세요.
    """
    # ASSUMPTION: 아래는 예시입니다. 실제 DB 조회로 교체하세요.
    # user = await get_user_by_email(db, body.email)
    # if not user or not verify_password(body.password, user.password):
    #     raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 올바르지 않습니다.")

    logger.info("login_attempt", email=body.email)

    # TODO: 실제 인증 로직 구현 전 임시 처리
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="로그인 로직을 구현해주세요.",
    )


@router.post("/refresh", response_model=TokenResponse, summary="토큰 갱신")
async def refresh_token(body: RefreshRequest) -> TokenResponse:
    """Refresh Token으로 새로운 Access Token을 발급합니다."""
    payload = verify_token(body.refresh_token, expected_type="refresh")
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh Token이 유효하지 않습니다.",
        )

    subject = payload["sub"]
    logger.info("token_refreshed", user=subject)

    return TokenResponse(
        access_token=create_access_token(subject),
        refresh_token=create_refresh_token(subject),
    )
