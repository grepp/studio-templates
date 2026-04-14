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
5. 기존 `README.md`가 있으면 `README.md.bak`으로 백업한다

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

2. **DESIGN.md** — 시스템 설계 템플릿
   ```bash
   curl -s ${BASE_URL}/DESIGN.md
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
    ├── DESIGN.md
    ├── RUNBOOK.md
    └── SECURITY.md
```

#### AGENTS.md (루트)

fetch 한 `AGENTS.md` 내용을 **그대로** 프로젝트 루트에 생성한다. 수정하지 않는다.
이 파일은 이후 AI Agent가 프로젝트에서 작업할 때 항상 참조하는 기준 문서다.

#### .grepp-agent/ 디렉토리

`.grepp-agent/` 디렉토리를 생성하고, 아래 파일들을 프로젝트에 맞게 수정하여 넣는다:

**DESIGN.md** — fetch 한 템플릿을 기반으로 다음을 반영하여 작성:
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

다음 파일을 대상 프로젝트에 맞게 생성한다:

| 파일 | 조건 | 작성 기준 |
|------|------|-----------|
| `Dockerfile` | 항상 | 대상 언어에 맞는 베이스 이미지, 멀티스테이지 빌드, non-root 실행 |
| `docker-compose.yml` | DB 또는 외부 서비스가 필요한 경우 | 대상 프로젝트가 사용하는 DB 엔진에 맞게 작성 |
| `.gitignore` | 항상 (기존 파일이 없거나 `.env` 미포함 시 보완) | 언어에 맞는 기본 항목 + `.env` 반드시 포함 |
| `.dockerignore` | 항상 | `.env`, `.git`, 문서 파일 제외 |
| 의존성 파일 | 항상 | `requirements.txt` / `package.json` / `Gemfile` 등 언어에 맞는 것 |
| `.env.example` | 기존에 없는 경우 | 대상 프로젝트가 실제로 사용하는 환경 변수만 |

**Helm Chart** — Kubernetes 배포가 필요한 프로젝트인 경우에만 생성. 이 템플릿의 `helm/` 디렉토리를 참고하되, 대상 프로젝트의 포트·리소스·환경 변수에 맞게 수정.

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
- `.env`가 `.gitignore`에 포함되어 있는지 확인
- 로그에 민감정보(비밀번호, 토큰, 개인정보)가 출력되지 않는지 확인
- 여러 사용자가 접근하는데 인증 구조가 없으면 추가

### Step 5: 사용자 인터뷰

파일 생성과 보안 검사가 끝났으면, 사용자에게 다음 질문을 하라:

```
프로젝트 템플릿 적용이 거의 완료되었습니다.
README.md 작성을 위해 몇 가지 확인이 필요합니다:

1. 서비스명이 무엇인가요?
2. 한 줄로 서비스를 설명해주세요.
3. 서비스의 주요 목적은 무엇인가요?
4. 주요 기능은 무엇인가요? (2~5개)
5. 사용 대상은 누구인가요?
6. 개발 담당자 이름과 연락처를 알려주세요. (선택)
7. 운영 담당자 이름과 연락처를 알려주세요. (선택)
8. 외부 서비스와 연동하나요? (있다면 어떤 서비스인가요?)
```

### Step 6: README.md 생성

사용자의 답변을 바탕으로, fetch 한 `template-README.md` 템플릿을 채워서 프로젝트 루트에 `README.md`를 생성한다.

기존 `README.md`가 있었다면 Step 0에서 `README.md.bak`으로 백업해두었을 것이다. 생성 완료 후 사용자에게 백업 파일 존재를 알려라.

### Step 7: 완료

모든 작업이 끝났으면, 사용자에게 다음을 보고하라:

```
✅ 프로젝트 템플릿 적용이 완료되었습니다.

생성된 파일:
- AGENTS.md               (AI 작업 기준 문서)
- .grepp-agent/DESIGN.md  (시스템 설계 문서)
- .grepp-agent/RUNBOOK.md (운영 절차서)
- .grepp-agent/SECURITY.md (보안 정책 문서)
- README.md               (프로젝트 소개 문서)

⚠️ TODO 항목이 포함된 파일이 있습니다. 담당자가 확인 후 내용을 채워주세요.
📁 기존 README.md는 README.md.bak으로 백업되었습니다. (해당 시)

이후 AI로 코드 작업 시 AGENTS.md가 자동으로 참조됩니다.
```

### ⚠️ Warning

**사용자가 명시적으로 요청하지 않았으면, 기존 비즈니스 로직을 수정하지 마라.** 이 템플릿의 목적은 운영 구조를 추가하는 것이지, 기능을 변경하는 것이 아니다.
