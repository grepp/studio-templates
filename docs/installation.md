# Installation

## For Humans

AI Agent에게 다음을 복사해서 붙여넣으세요:

```
Fetch and follow the installation guide:
curl -fsSL https://raw.githubusercontent.com/grepp/studio-templates/refs/heads/nagle/installation-structure-design/docs/installation.md
```

직접 하지 마세요. AI가 하는 게 더 빠르고 정확합니다.

---

## For LLM Agents

> **IMPORTANT: Use `curl` to fetch this file, NOT WebFetch.** WebFetch summarizes content and loses critical details like security checks and user interview questions. Always use:
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/grepp/studio-templates/refs/heads/nagle/installation-structure-design/docs/installation.md
> ```

이 문서를 읽고 있다면, 당신은 비개발자의 프로젝트에 운영 표준 템플릿을 적용하려는 AI Agent입니다. 사용자의 프로젝트를 분석하고, 실행·배포 가능한 서비스 구조로 변환하세요.

다음 스텝을 순서대로 따르세요:

### Step 0: 프로젝트 분석

먼저 대상 프로젝트의 현재 상태를 파악하세요:

1. 프로젝트 루트 디렉토리를 확인한다
2. 사용 중인 언어와 프레임워크를 파악한다
3. 기존 디렉토리 구조를 파악한다
4. 다음 파일의 존재 여부를 확인한다:
   - `.env` / `.env.example`
   - `Dockerfile` / `docker-compose.yml`
   - `.gitignore` / `.dockerignore`
   - `README.md`

### Step 1: 템플릿 문서 fetch

다음 파일들을 순차적으로 fetch하여 읽는다. 모두 같은 base URL 아래에 있다:

```bash
BASE_URL=https://raw.githubusercontent.com/grepp/studio-templates/refs/heads/nagle/installation-structure-design/docs
```

**반드시 읽어야 하는 파일 (순서대로):**

1. **AGENTS.md** — AI 작업 기준 문서 (핵심)
   ```bash
   curl -s ${BASE_URL}/AGENTS.md
   ```

2. **ARCHITECTURE.md** — 시스템 구조 템플릿
   ```bash
   curl -s ${BASE_URL}/ARCHITECTURE.md
   ```

3. **RUNBOOK.md** — 운영 절차서 템플릿
   ```bash
   curl -s ${BASE_URL}/RUNBOOK.md
   ```

4. **SECURITY.md** — 보안 정책 템플릿
   ```bash
   curl -s ${BASE_URL}/SECURITY.md
   ```

5. **template-README.md** — README 템플릿
   ```bash
   curl -s ${BASE_URL}/template-README.md
   ```

### Step 2: 파일 생성

대상 프로젝트에 다음 구조로 파일을 생성한다:

```
대상 프로젝트/
├── AGENTS.md                    ← 루트
├── README.md                    ← 루트 (Step 5에서 생성)
└── .grepp-agent/
    ├── ARCHITECTURE.md
    ├── RUNBOOK.md
    └── SECURITY.md
```

#### AGENTS.md (루트)

fetch 한 `AGENTS.md` 내용을 **그대로** 프로젝트 루트에 생성한다. 수정하지 않는다.
이 파일은 이후 AI Agent가 프로젝트에서 작업할 때 항상 참조하는 기준 문서다.

#### .grepp-agent/ 디렉토리

`.grepp-agent/` 디렉토리를 생성하고, 아래 파일들을 프로젝트에 맞게 수정하여 넣는다:

**ARCHITECTURE.md** — fetch 한 템플릿을 기반으로 다음을 반영하여 작성:
- 프로젝트의 실제 구조에 맞는 시스템 구조도
- 프로젝트의 실제 데이터 흐름
- 프로젝트의 실제 외부 연동 서비스
- 인증 구조가 없으면 "해당 없음"으로 명시
- 모르는 항목은 `TODO:` 마커로 표시

**RUNBOOK.md** — fetch 한 템플릿을 기반으로 다음을 반영하여 작성:
- 서비스명을 실제 프로젝트명으로 교체
- 담당자 정보를 `TODO:`로 표시
- 프로젝트에 맞는 배포 방법

**SECURITY.md** — fetch 한 템플릿을 기반으로 다음을 반영하여 작성:
- 실제 수집 데이터 목록
- 실제 외부 전송 데이터
- 모르는 항목은 `TODO:` 마커로 표시

### Step 3: 인프라 파일 생성

> **주의: 이 템플릿 저장소의 `app/`, `src/`, `docker/`, `helm/`은 Python/FastAPI/PostgreSQL 기준 예시다. 대상 프로젝트의 언어·프레임워크·DB에 맞게 새로 작성하라. 예시를 그대로 복사하지 마라.**

#### Dockerfile (강제)

**모든 프로젝트에 Dockerfile을 생성한다. 예외 없다.**

- 서버 애플리케이션: 앱 서버 컨테이너로 빌드 (예: Python → uvicorn, Node.js → express)
- 정적 파일 프로젝트(HTML/JS/CSS): Nginx 컨테이너로 정적 호스팅
- 공통 사항: 멀티스테이지 빌드, non-root 실행, HEALTHCHECK 포함

#### 민감정보 분리 파일

프로젝트 환경에 맞는 방식 **하나만** 선택하여 생성한다. 여러 방식을 중복하지 마라.

| 환경 | 선택할 방식 | 예시 파일 (커밋됨) | 실제 파일 (.gitignore 등록) |
|------|------------|-------------------|---------------------------|
| 서버 런타임 (Node.js, Python 등) | `.env` | `.env.example` | `.env` |
| 브라우저 only (HTML/JS) | JS 설정 파일 | `app-config.example.js` | `app-config.js` |
| 빌드 도구 사용 (Vite, webpack 등) | `.env` + 빌드 주입 | `.env.example` | `.env` |

**반드시 두 파일 모두 생성해야 한다:**

1. **예시 파일** (`.example`) — dummy 값으로 Git에 커밋
2. **실제 파일** — 소스 코드에서 추출한 **실제 값** 그대로 입력

```
예: 브라우저 프로젝트의 경우
├── app-config.example.js   ← dummy 값 (Git 커밋됨)
└── app-config.js           ← 실제 값 (Git 제외)
```

> **절대 소스 코드에서 기존 값을 삭제하지 마라.** 기존 API Key, 비밀번호 등은 실제 파일로 그대로 옮겨야 한다. 앱이 바로 동작해야 한다.
> 기존 값이 이미 Git에 커밋된 적이 있으면 사용자에게 재발급을 권고하되, **임의로 값을 지우거나 dummy로 교체하지 마라.**

자세한 기준은 `AGENTS.md` §4.2를 참고하라.

#### 나머지 인프라 파일

| 파일 | 조건 | 작성 기준 |
|------|------|-----------|
| `docker-compose.yml` | DB 또는 외부 서비스가 필요한 경우 | 대상 프로젝트가 사용하는 DB 엔진에 맞게 작성 |
| `.gitignore` | 항상 (기존 파일이 없거나 민감 파일 미포함 시 보완) | 언어에 맞는 기본 항목 + 실제 설정 파일(예: `.env`, `app-config.js`) 반드시 포함 |
| `.dockerignore` | 항상 | 민감 파일, `.git`, 문서 파일 제외 |
| 의존성 파일 | 항상 | `requirements.txt` / `package.json` / `Gemfile` 등 언어에 맞는 것 |

**디렉토리 구조** — 다음을 권장하되, 기존 구조가 합리적이면 유지하고 필요한 부분만 보완:

```
/app          — 애플리케이션 진입점
/src          — 비즈니스 로직 및 공통 모듈
/config       — 환경별 설정 파일
/docker       — 컨테이너 관련 (Dockerfile, docker-compose.yml)
/helm         — Kubernetes 배포 (선택)
```

### Step 4: 보안 검사

`AGENTS.md` §4와 `SECURITY.md`를 기준으로 다음을 검사한다. 위반 항목이 있으면 수정하고 사용자에게 보고하라:

- 코드에 하드코딩된 비밀번호 / API Key가 없는지 확인
  - 발견 시: 값을 **실제 파일(.env, app-config.js 등)로 옮기고** 소스 코드에서는 참조로 대체한다
  - **절대 값을 삭제하거나 dummy로 교체하지 마라.** 앱이 동작해야 한다
- 실제 설정 파일이 `.gitignore`에 포함되어 있는지 확인
- 로그에 민감정보(비밀번호, 토큰, 개인정보)가 출력되지 않는지 확인
- 여러 사용자가 접근하는데 인증 구조가 없으면 추가

### Step 5: 사용자 인터뷰

파일 생성과 보안 검사가 끝났으면, 사용자에게 질문을 **하나씩** 전달하여 답변을 받는다.
모든 질문을 한 번에 보내지 마라. 하나의 질문에 답변을 받은 후 다음 질문으로 넘어간다.

**질문 순서:**

1. "서비스명이 무엇인가요?"
2. "서비스의 주요 목적과 핵심 기능(2~5개)을 알려주세요."
3. "사용 대상은 누구인가요?"
4. "개발 담당자 이름과 연락처를 알려주세요. (선택)"
5. "운영 담당자 이름과 연락처를 알려주세요. (선택)"
6. "외부 서비스와 연동하나요? (있다면 어떤 서비스인가요?)"

### Step 6: 문서 TODO 채우기

Step 2에서 생성한 ARCHITECTURE.md, RUNBOOK.md, SECURITY.md에 남아있는 `TODO:` 항목을 사용자의 답변으로 채운다.

채울 수 없는 항목은 사용자에게 **추가로 질문**하여 입력받는다. 예:

- ARCHITECTURE.md의 외부 연동 서비스 → Step 5의 8번 답변으로 채움
- RUNBOOK.md의 담당자 → Step 5의 6, 7번 답변으로 채움
- SECURITY.md의 수집 데이터 → 사용자에게 "이 서비스에서 수집하는 데이터가 있나요?" 라고 추가 질문

모든 `TODO:` 항목이 채워질 때까지 사용자와 대화하며 완성한다.

### Step 7: README.md 생성

사용자의 답변을 바탕으로, fetch 한 `template-README.md` 템플릿을 채워서 프로젝트 루트에 `README.md`를 생성한다.
기존 `README.md`가 있었다면 덮어쓴다.

### Step 8: 완료

모든 작업이 끝났으면, 사용자에게 다음을 보고하라:

```
✅ 프로젝트 템플릿 적용이 완료되었습니다.

생성된 파일:
- AGENTS.md               (AI 작업 기준 문서)
- .grepp-agent/ARCHITECTURE.md  (시스템 구조 문서)
- .grepp-agent/RUNBOOK.md (운영 절차서)
- .grepp-agent/SECURITY.md (보안 정책 문서)
- README.md               (프로젝트 소개 문서)

🔑 민감정보 처리 안내:
- 소스 코드의 API Key 등은 {실제 파일}로 분리되었습니다.
- 기존 값은 그대로 보존되어 있으므로 앱이 바로 동작합니다.
- {실제 파일}은 .gitignore에 등록되어 Git에 커밋되지 않습니다.
- ⚠️ 기존 값이 Git에 커밋된 적이 있다면 즉시 재발급받으세요.
  재발급 후 {실제 파일}의 값을 새 값으로 교체해야 합니다.

이후 AI로 코드 작업 시 AGENTS.md가 자동으로 참조됩니다.
```

### ⚠️ Warning

**사용자가 명시적으로 요청하지 않았으면, 기존 비즈니스 로직을 수정하지 마라.** 이 템플릿의 목적은 운영 구조를 추가하는 것이지, 기능을 변경하는 것이 아니다.
