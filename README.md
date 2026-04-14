# Installation Structure Design Template

> 비개발자가 AI로 생성한 코드를, 회사 운영 표준에 맞는 프로덕션 서비스로 변환하는 템플릿.

---

## 개요

이 저장소는 **템플릿**이다. 비개발자의 프로젝트에 적용하면:

- `AGENTS.md` — AI가 따라야 할 작업 기준 문서
- `DESIGN.md` — 시스템 설계 템플릿
- `RUNBOOK.md` — 운영 절차서 템플릿
- `SECURITY.md` — 보안 정책 템플릿
- 디렉토리 구조, Dockerfile, Helm Chart 등 운영 인프라 일식

이 생성된다.

### 기술 스택

| 항목 | 기본값 |
|------|--------|
| 언어 | Python |
| 프레임워크 | FastAPI |
| DB | PostgreSQL 16.x |
| 컨테이너 | Docker (멀티스테이지 빌드) |
| 배포 | Kubernetes / Helm |
| 인증 | JWT (HS256) |
| 로깅 | structlog (JSON 구조화) |

---

## Installation

### For LLM Agents

AI Agent에게 다음을 지시하세요:

```
Fetch and follow the installation guide:
curl -s https://raw.githubusercontent.com/grepp/studio-templates/refs/heads/nagle/installation-structure-design/docs/installation.md
```

또는:

```
Read this and apply the template to my project:
https://raw.githubusercontent.com/grepp/studio-templates/refs/heads/nagle/installation-structure-design/docs/installation.md
```

### For Humans

직접 설치하고 싶다면 `docs/installation.md`를 읽고 수동으로 진행하세요.
하지만 AI Agent에게 맡기는 것을 권장합니다.

---

## 템플릿 구조

```
/
├── docs/                  ← 템플릿 문서
│   ├── installation.md   ← AI가 curl로 fetch하는 설치 가이드
│   ├── AGENTS.md         ← AI 작업 기준 문서 (대상 프로젝트에 복사됨)
│   ├── DESIGN.md         ← 시스템 설계 템플릿
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
AI: AGENTS.md, DESIGN.md, RUNBOOK.md, SECURITY.md 순차 fetch
  ↓
AI: 대상 프로젝트 분석 → 파일 생성 → 구조 정리 → 보안 검사
  ↓
AI: 사용자에게 정보 질문 (서비스명, 목적, 담당자 등)
  ↓
AI: README.md 생성 → 완료 보고
```

### 설치 결과 (대상 프로젝트)

```
대상 프로젝트/
├── AGENTS.md                    ← 루트 (AI 도구 자동 인식)
├── README.md                    ← 루트 (사용자 인터뷰 기반 생성)
└── .grepp-agent/
    ├── DESIGN.md                ← 시스템 설계 문서
    ├── RUNBOOK.md               ← 운영 절차서
    └── SECURITY.md              ← 보안 정책 문서
```


