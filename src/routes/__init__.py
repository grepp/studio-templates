"""
API 라우터 통합 등록.
새 라우터 추가 시 이 파일에 include_router로 등록하세요.
"""
from fastapi import APIRouter

from src.routes.auth import router as auth_router

# TODO: 추가 라우터를 아래에 등록하세요
# from src.routes.users import router as users_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["auth"])
# router.include_router(users_router, prefix="/users", tags=["users"])
