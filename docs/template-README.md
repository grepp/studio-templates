# 서비스명 (Service Name)

> 한 줄 서비스 설명을 여기에 작성하세요.

---

## 목차

- [서비스 개요](#서비스-개요)
- [실행 방법](#실행-방법)
- [환경 변수](#환경-변수)
- [API 엔드포인트](#api-엔드포인트)
- [담당자](#담당자)

---

## 서비스 개요

<!-- TODO: 서비스의 목적, 주요 기능, 사용 대상을 작성하세요 -->

| 항목 | 내용 |
|------|------|
| 서비스명 | - |
| 목적 | - |
| 주요 기능 | - |
| 사용 대상 | - |
| 기술 스택 | Python / FastAPI / PostgreSQL 16 |

---

## 실행 방법

### 로컬 개발 환경

```bash
# 1. 환경 변수 설정
cp .env.example .env
# .env 파일을 열어 값 입력

# 2. 의존성 설치
pip install -r requirements.txt

# 3. 서버 실행
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Docker 실행

```bash
# 빌드
docker build -f docker/Dockerfile -t service-name:latest .

# 실행
docker run --env-file .env -p 8000:8000 service-name:latest
```

### Docker Compose 실행 (앱 + DB 포함)

```bash
docker compose -f docker/docker-compose.yml up -d
```

---

## 환경 변수

`.env.example` 파일을 참고하세요. 실제 값은 `.env` 파일에 설정하며 Git에 커밋하지 않습니다.

| 변수명 | 설명 | 예시 |
|--------|------|------|
| `APP_ENV` | 실행 환경 | `development` / `production` |
| `APP_PORT` | 서버 포트 | `8000` |
| `SECRET_KEY` | JWT 서명 키 | *(임의 생성값)* |
| `DATABASE_URL` | PostgreSQL 연결 문자열 | `postgresql://user:pass@host:5432/db` |
| `LOG_LEVEL` | 로그 레벨 | `INFO` / `DEBUG` |

전체 목록은 [`.env.example`](.env.example) 참고.

---

## API 엔드포인트

| Method | Path | 설명 | 인증 필요 |
|--------|------|------|-----------|
| GET | `/health` | 헬스체크 | 불필요 |
| POST | `/auth/login` | 로그인 (JWT 발급) | 불필요 |
| GET | `/api/v1/...` | 주요 API | 필요 |

전체 API 문서: 실행 후 `http://localhost:8000/docs` 접속

---

## 담당자

| 역할 | 이름 | 연락처 |
|------|------|--------|
| 개발 | <!-- TODO --> | - |
| 운영 | <!-- TODO --> | - |

---

> 이 프로젝트는 [AGENTS.md](AGENTS.md) 기준을 따릅니다.
