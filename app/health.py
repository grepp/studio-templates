"""
헬스체크 엔드포인트.
로드밸런서 및 Kubernetes liveness/readiness probe에서 사용합니다.
"""
from fastapi import APIRouter
from sqlalchemy import text

from src.db.session import get_db_session
from src.logger import get_logger

router = APIRouter(tags=["health"])
logger = get_logger(__name__)


@router.get("/health", summary="헬스체크")
async def health_check():
    """서비스 정상 동작 여부를 반환합니다."""
    return {"status": "ok"}


@router.get("/health/ready", summary="Readiness 체크")
async def readiness_check():
    """DB 연결을 포함한 전체 준비 상태를 반환합니다."""
    db_status = "ok"
    try:
        async with get_db_session() as session:
            await session.execute(text("SELECT 1"))
    except Exception as e:
        logger.error("readiness_check_failed", error=str(e))
        db_status = "error"

    overall = "ok" if db_status == "ok" else "degraded"
    return {
        "status": overall,
        "checks": {
            "database": db_status,
        },
    }
