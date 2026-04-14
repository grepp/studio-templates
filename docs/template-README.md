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

## 설정

민감정보(API Key, 비밀번호 등)는 코드에서 분리되어 있습니다.
프로젝트에 포함된 예시 파일을 복사하여 실제 값을 입력하세요.

<!-- TODO: 프로젝트에 맞는 분리 방식의 안내만 남기고 나머지는 삭제하세요 -->

### 서버 프로젝트인 경우

```bash
cp .env.example .env
# .env 파일을 열어 실제 값을 입력하세요. .env는 Git에 커밋하지 않습니다.
```

### 브라우저 only 프로젝트인 경우

```bash
cp app-config.example.js app-config.js
# app-config.js 파일을 열어 실제 값을 입력하세요. 이 파일은 Git에 커밋하지 않습니다.
```

> ⚠️ 기존에 소스 코드에 포함되어 있던 API Key, 비밀번호 등은 분리 과정에서 제거되었습니다.
> 해당 값이 이미 Git에 커밋된 적이 있다면 **즉시 재발급**받으세요.

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
