-- init.sql — Docker 로컬 개발용 초기 DB 스크립트
-- 운영 DB에 직접 적용하지 마세요. 마이그레이션은 Alembic으로 관리합니다.

-- UUID 확장 활성화
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 예시: users 테이블
-- TODO: 실제 스키마로 교체하세요
CREATE TABLE IF NOT EXISTS users (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email       VARCHAR(255) UNIQUE NOT NULL,
    password    VARCHAR(255) NOT NULL,
    role        VARCHAR(50) NOT NULL DEFAULT 'user',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 개발용 더미 관리자 계정 (비밀번호: changeme — 운영 환경 절대 사용 금지)
-- INSERT INTO users (email, password, role)
-- VALUES ('admin@example.com', '$2b$12$dummy_hash_replace_me', 'admin');
