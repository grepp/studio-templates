# =============================================================================
# Dockerfile — 멀티스테이지 빌드
# 빌드: docker build -f docker/Dockerfile -t service-name:latest .
# 실행: docker run --env-file .env -p 8000:8000 service-name:latest
# =============================================================================

# Stage 1: 의존성 빌드
FROM python:3.12-slim AS builder

WORKDIR /build

# 시스템 패키지 (psycopg2 빌드용)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: 실행 이미지 (최소 크기)
FROM python:3.12-slim AS runtime

# 보안: root 외 사용자로 실행
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

# 시스템 패키지 (psycopg2 런타임)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# 빌드 스테이지에서 설치된 패키지 복사
COPY --from=builder /install /usr/local

# 소스 코드 복사 (민감 파일 제외 — .dockerignore 참고)
COPY app/ ./app/
COPY src/ ./src/
COPY config/ ./config/

# 소유권 변경
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
