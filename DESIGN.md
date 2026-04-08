# DESIGN.md — 시스템 설계 문서

> 이 문서는 서비스의 구조, 데이터 흐름, 외부 연동, 인증 방식을 기술합니다.

---

## 1. 시스템 구조

```
┌─────────────────────────────────────────────────────┐
│                    Client (Browser / App)            │
└──────────────────────────┬──────────────────────────┘
                           │ HTTPS
┌──────────────────────────▼──────────────────────────┐
│               Load Balancer / Ingress                │
└──────────────────────────┬──────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────┐
│             FastAPI Application (app/)               │
│                                                      │
│  ┌─────────────┐  ┌───────────┐  ┌───────────────┐  │
│  │   Routes    │  │   Auth    │  │    Logger     │  │
│  │ /api/v1/... │  │  JWT/Session│  │  Structured  │  │
│  └──────┬──────┘  └─────┬─────┘  └───────────────┘  │
│         └───────────────┘                            │
│                   │                                  │
│  ┌────────────────▼──────────────────────────────┐  │
│  │              Service Layer (src/)             │  │
│  └────────────────┬──────────────────────────────┘  │
└───────────────────┼──────────────────────────────────┘
                    │
        ┌───────────▼────────────┐
        │   PostgreSQL 16.x      │
        │   (DB / RDS)           │
        └────────────────────────┘
```

### 디렉토리 구조

```
/
├── app/                  # 애플리케이션 진입점
│   ├── main.py           # FastAPI 앱 초기화, 라우터 등록
│   └── health.py         # 헬스체크 엔드포인트
│
├── src/                  # 비즈니스 로직 및 공통 모듈
│   ├── config.py         # 환경 변수 파싱
│   ├── logger.py         # 로그 설정
│   ├── auth/             # 인증 모듈 (JWT)
│   ├── db/               # DB 연결 및 ORM 모델
│   └── routes/           # API 라우터
│
├── config/               # 환경별 설정 파일 (yaml)
│   ├── app.yaml
│   └── logging.yaml
│
├── docker/               # 컨테이너 관련
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── helm/                 # Kubernetes 배포
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│
├── .env.example          # 환경 변수 예시
├── requirements.txt      # Python 의존성
├── README.md
├── DESIGN.md             # (이 문서)
├── RUNBOOK.md
└── SECURITY.md
```

---

## 2. 데이터 흐름

### 일반 API 요청 흐름

```
Client
  → [HTTPS 요청]
  → Ingress / Load Balancer
  → FastAPI Router
  → Auth Middleware (JWT 검증)
  → Service Layer (비즈니스 로직)
  → DB Layer (PostgreSQL)
  → JSON 응답 반환
```

### 인증 흐름

```
Client
  → POST /auth/login { username, password }
  → 사용자 조회 (DB)
  → 비밀번호 검증 (bcrypt)
  → JWT Access Token 발급 (만료: 1시간)
  → JWT Refresh Token 발급 (만료: 7일)
  → 응답: { access_token, refresh_token }
```

---

## 3. 외부 연동

<!-- TODO: 실제 연동하는 외부 서비스가 있으면 아래 표를 채워주세요 -->

| 서비스 | 용도 | 인증 방식 | 비고 |
|--------|------|-----------|------|
| - | - | API Key (환경 변수) | - |

> 외부 API로 전송되는 데이터 종류를 명시해야 합니다. 개인정보·민감정보는 전송 금지.

---

## 4. 인증 구조

| 항목 | 내용 |
|------|------|
| 방식 | JWT (Access + Refresh Token) |
| 서명 알고리즘 | HS256 |
| Access Token 만료 | 1시간 |
| Refresh Token 만료 | 7일 |
| 저장 위치 | 클라이언트 메모리 / HttpOnly Cookie |
| 사용자 권한 | `admin` / `user` |

---

## 5. 데이터베이스

| 항목 | 내용 |
|------|------|
| DBMS | PostgreSQL 16.x |
| ORM | SQLAlchemy 2.x |
| 마이그레이션 | Alembic |
| 연결 방식 | 환경 변수 `DATABASE_URL` |

### 주요 테이블

<!-- TODO: 실제 테이블 구조를 작성하세요 -->

```sql
-- 예시: users 테이블
CREATE TABLE users (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email       VARCHAR(255) UNIQUE NOT NULL,
    password    VARCHAR(255) NOT NULL,  -- bcrypt 해시
    role        VARCHAR(50) DEFAULT 'user',
    created_at  TIMESTAMP DEFAULT NOW(),
    updated_at  TIMESTAMP DEFAULT NOW()
);
```

---

## 6. 비기능 요건

| 항목 | 기준 |
|------|------|
| 응답시간 | p99 < 500ms |
| 가용성 | 99.9% |
| 로그 보존 | 30일 |
| 민감정보 로그 | 금지 |

---

> ASSUMPTION: DB는 단일 PostgreSQL 인스턴스 기준. 고가용성 필요 시 별도 구성 필요.
