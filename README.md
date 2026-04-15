# Installation Structure Design Template

> 비개발자가 AI로 생성한 코드를, 회사 운영 표준에 맞는 프로덕션 서비스로 변환하는 템플릿.

---

## 개요

이 저장소는 **템플릿**이다. 비개발자의 프로젝트에 적용하면:

- `AGENTS.md` — AI가 따라야 할 작업 기준 문서
- `ARCHITECTURE.md` — 시스템 구조 템플릿
- `RUNBOOK.md` — 운영 절차서 템플릿
- `SECURITY.md` — 보안 정책 템플릿
- `SPEC.md` — 서비스 명세서 (초기 프로젝트 한정)
- 디렉토리 구조, Dockerfile, Helm Chart 등 운영 인프라 일식

이 생성된다.

### 기술 스택

| 항목       | 기본값                     |
| ---------- | -------------------------- |
| 언어       | Python                     |
| 프레임워크 | FastAPI                    |
| DB         | PostgreSQL 16.x            |
| 컨테이너   | Docker (멀티스테이지 빌드) |
| 배포       | Kubernetes / Helm          |
| 인증       | JWT (HS256)                |
| 로깅       | structlog (JSON 구조화)    |

---

## Installation

사용하고 있는 AI Agent에게 다음을 지시하세요:

```
Fetch and follow the installation guide:
curl -s https://raw.githubusercontent.com/grepp/studio-templates/refs/heads/main/docs/installation.md
```

---

## 템플릿 구조

```
/
├── .github/workflows/
│   └── bump-version.yml  ← main push 시 VERSION 자동 갱신
├── docs/                  ← 템플릿 문서
│   ├── VERSION           ← 템플릿 버전 (GitHub Action이 자동 갱신)
│   ├── update.md         ← 업데이트 절차 가이드
│   ├── installation.md   ← AI가 curl로 fetch하는 설치 가이드
│   ├── AGENTS.md         ← AI 작업 기준 문서 (대상 프로젝트에 복사됨)
│   ├── ARCHITECTURE.md   ← 시스템 구조 템플릿
│   ├── RUNBOOK.md        ← 운영 절차서 템플릿
│   ├── SECURITY.md       ← 보안 정책 템플릿
│   └── template-README.md ← 대상 프로젝트용 README 템플릿
│
├── app/                  ← 애플리케이션 진입점
│   ├── main.py
│   └── health.py
├── src/                  ← 비즈니스 로직
│   ├── config.py
│   ├── logger.py
│   ├── auth/
│   ├── db/
│   └── routes/
├── config/               ← 환경별 설정
├── docker/               ← 컨테이너 정의
├── helm/                 ← Kubernetes 배포
│
├── .env.example
├── requirements.txt
├── .gitignore
└── .dockerignore
```

---

## 설치 플로우

```
사용자: "이 템플릿을 내 프로젝트에 적용해"
  ↓
AI: curl installation.md → 읽기
  ↓
AI: VERSION, AGENTS.md, ARCHITECTURE.md, RUNBOOK.md, SECURITY.md 순차 fetch
  ↓
AI: 대상 프로젝트 분석 → 파일 생성 → 구조 정리 → 보안 검사
  ↓
AI: 사용자에게 정보 질문 (서비스명, 목적, 민감 데이터 여부, 담당자 등)
  ↓
AI: README.md 생성 → 완료 보고
  ↓
[초기 프로젝트인 경우] 추가 질문 → SPEC.md 작성 → 구현 승인
```

### 세션 시작 시 자동 버전 체크

AI Agent는 **첫 번째 요청** 시 자동으로 템플릿 버전을 확인한다:

```
Agent 세션 시작
  ↓
로컬 .grepp-agent/VERSION vs 원격 VERSION 비교
  ↓
새 버전 있음 → update.md fetch → 변경사항 비교 → 사용자 확인 후 업데이트
버전 동일   → 바로 작업 진행
```

### 민감 데이터 보호

사용자가 개발자가 아닌 점을 고려하여, AI Agent가 **능동적으로** 다음 상황을 감시한다:

- 개인정보 또는 회사 민감 데이터 처리 감지 시 → [Slack 채널](https://grepp.slack.com/archives/C02C3QKHEU8) 에스컬레이션
- 외부 DB, 클라우드 서비스 사용 감지 시 → 동일 에스컬레이션

### 설치 결과 (대상 프로젝트)

```
대상 프로젝트/
├── AGENTS.md                    ← 루트 (AI 도구 자동 인식)
├── README.md                    ← 루트 (사용자 인터뷰 기반 생성)
└── .grepp-agent/
    ├── VERSION                  ← 설치된 템플릿 버전 (업데이트 확인용)
    ├── ARCHITECTURE.md          ← 시스템 구조 문서
    ├── RUNBOOK.md               ← 운영 절차서
    ├── SECURITY.md              ← 보안 정책 문서
    └── SPEC.md                  ← 서비스 명세서 (초기 프로젝트만)
```
