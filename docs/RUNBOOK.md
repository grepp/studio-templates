# RUNBOOK.md — 운영 절차서

> 이 문서는 배포, 재시작, 장애 대응 절차를 기술합니다.  
> 운영 중 문제 발생 시 이 문서를 먼저 참고하세요.

---

## 1. 배포 방법

### 1.1 Docker 단독 배포

```bash
# 이미지 빌드
docker build -f docker/Dockerfile -t service-name:$(git rev-parse --short HEAD) .

# 실행 (환경 변수 파일 사용)
docker run -d \
  --name service-name \
  --env-file .env \
  -p 8000:8000 \
  --restart unless-stopped \
  service-name:latest
```

### 1.2 Helm (Kubernetes) 배포

```bash
# 네임스페이스 생성 (최초 1회)
kubectl create namespace my-service

# Secret 생성 (최초 1회)
kubectl create secret generic my-service-secret \
  --from-literal=SECRET_KEY="your-secret-key" \
  --from-literal=DATABASE_URL="postgresql://..." \
  -n my-service

# 배포
helm upgrade --install my-service ./helm \
  -f helm/values.yaml \
  --set image.tag=$(git rev-parse --short HEAD) \
  -n my-service

# 배포 상태 확인
kubectl rollout status deployment/my-service -n my-service
```

### 1.3 배포 후 확인

```bash
# 헬스체크
curl http://localhost:8000/health

# 로그 확인
kubectl logs -l app=my-service -n my-service --tail=100 -f
```

---

## 2. 재시작 방법

### Docker 재시작

```bash
docker restart service-name
```

### Kubernetes 재시작

```bash
# 롤링 재시작 (무중단)
kubectl rollout restart deployment/my-service -n my-service

# 상태 확인
kubectl rollout status deployment/my-service -n my-service
```

---

## 3. 롤백 방법

### Docker 롤백

```bash
# 이전 태그로 컨테이너 재실행
docker stop service-name && docker rm service-name
docker run -d --name service-name --env-file .env -p 8000:8000 service-name:이전태그
```

### Helm 롤백

```bash
# 배포 이력 확인
helm history my-service -n my-service

# 특정 리비전으로 롤백
helm rollback my-service [REVISION] -n my-service
```

---

## 4. 장애 대응

### 4.1 서비스 응답 없음 (5xx / timeout)

```bash
# 1. Pod 상태 확인
kubectl get pods -n my-service

# 2. 로그 확인
kubectl logs -l app=my-service -n my-service --tail=200

# 3. 이벤트 확인
kubectl describe pod <pod-name> -n my-service

# 4. 재시작
kubectl rollout restart deployment/my-service -n my-service
```

### 4.2 DB 연결 실패

```bash
# 1. 환경 변수 확인 (DATABASE_URL)
kubectl get secret my-service-secret -n my-service -o jsonpath='{.data.DATABASE_URL}' | base64 -d

# 2. DB Pod / RDS 상태 확인
kubectl get pods -l app=postgresql -n my-service

# 3. DB 연결 테스트
kubectl run -it --rm psql-test --image=postgres:16 --restart=Never \
  -- psql $DATABASE_URL -c "SELECT 1;"
```

### 4.3 메모리 / CPU 과부하

```bash
# 리소스 사용량 확인
kubectl top pods -n my-service

# HPA 상태 확인
kubectl get hpa -n my-service

# 수동 스케일아웃
kubectl scale deployment/my-service --replicas=3 -n my-service
```

### 4.4 인증 오류 (401 / 403 대량 발생)

- `SECRET_KEY` 환경 변수 변경 여부 확인
- JWT 만료 시간 설정 확인
- 클라이언트 토큰 갱신 여부 확인

---

## 5. 모니터링 체크리스트

| 항목 | 확인 방법 | 임계값 |
|------|-----------|--------|
| 헬스체크 | `GET /health` → 200 OK | - |
| 응답시간 | APM / CloudWatch | p99 < 500ms |
| 에러율 | 로그 / 대시보드 | 5xx < 1% |
| CPU | `kubectl top` | < 80% |
| 메모리 | `kubectl top` | < 80% |
| DB 연결 수 | PostgreSQL metrics | 최대 연결 수 80% 이하 |

---

## 6. 로그 확인

```bash
# 실시간 로그 스트리밍
kubectl logs -l app=my-service -n my-service -f

# 에러 로그만 필터
kubectl logs -l app=my-service -n my-service | grep '"level":"ERROR"'

# 특정 시간 이후 로그
kubectl logs -l app=my-service -n my-service --since=1h
```

---

## 7. 비상 연락처

<!-- TODO: 실제 담당자 정보로 채워주세요 -->

| 상황 | 담당자 | 연락처 |
|------|--------|--------|
| 서비스 장애 | 개발팀 담당자 | - |
| DB 장애 | DBA / 인프라팀 | - |
| 보안 이슈 | 보안 담당자 | - |
