# 🧩 Python ORM 라이브러리 비교표

| ORM 이름         | 비동기 지원 | 사용 환경            | 특징 요약                                                 | 마이그레이션 지원     | 라이선스    |
|------------------|--------------|------------------------|------------------------------------------------------------|------------------------|-------------|
| **SQLAlchemy**   | ✅ (Async 지원) | FastAPI, Flask 등      | 성능/유연성 최상, Core + ORM API, 실무 표준                | ✅ Alembic              | MIT         |
| **Django ORM**   | ❌ (비동기 부분적) | Django 전용           | 자동 admin/validation 내장, 완전 통합형 프레임워크         | ✅ Django migration     | BSD         |
| **Tortoise ORM** | ✅ 완전 지원   | FastAPI, Starlette 등  | 비동기 전용, Pydantic 친화적, Django 스타일 API            | ✅ Tortoise generate    | MIT         |
| **Peewee**       | ❌            | 경량 CLI, 소규모 앱    | 매우 간단하고 가벼움, SQLite/포스트그레SQL 등 지원         | ❌ (서드파티 불완전)    | MIT         |
| **Pony ORM**     | ❌            | 교육/테스트/소형 앱    | Python 식 쿼리 표현 (DSL), 직관적이나 느릴 수 있음         | ❌                     | Apache-2.0  |
| **Gino**         | ✅ 완전 지원   | FastAPI, Sanic         | SQLAlchemy 기반의 async ORM, Postgres 특화                | ❌ (Alembic 미지원)     | BSD         |
| **Ormantic**     | ✅            | FastAPI (단종)         | Pydantic 기반 ORM, 현재는 **Tortoise로 통합**              | ❌                     | MIT         |
| **Databases**    | ✅ (비ORM)     | SQLAlchemy Core + Async| ORM이 아닌 async DB 접근 계층 (FastAPI 등에서 보조로 사용) | ❌                     | BSD         |

---

## ✅ 주요 기준 설명

- **비동기 지원**: `async/await` 기반 ORM 여부 – FastAPI 사용 시 중요
- **사용 환경**: 어떤 프레임워크 또는 프로젝트 목적에 적합한지
- **마이그레이션**: Alembic, Django migrate 등 테이블 구조 변경 도구 제공 여부
- **라이선스**: 오픈소스 프로젝트에서 사용 가능 여부 확인

---

## 🔍 상황별 추천 ORM

| 조건 | 추천 ORM |
|------|----------|
| ✅ 실무용 / 확장성 필요 | **SQLAlchemy + Alembic** |
| ✅ FastAPI + 비동기 처리 | **Tortoise ORM**, **Gino** |
| ✅ Django 프로젝트 | **Django ORM** |
| ✅ 간단한 프로젝트 | **Peewee**, **Pony ORM** |

# 🚀 FastAPI ORM 선택 우선순위 요약표

| 우선순위 | ORM              | 특징                          | 마이그레이션 지원 | 비동기 지원     | 실무 적합성      |
|----------|------------------|-------------------------------|-------------------|------------------|------------------|
| 🥇 1     | **SQLAlchemy**   | 안정성, 확장성, 생태계 풍부  | ✅ Alembic         | ✅ (1.4 이상)     | ✅ 대규모 프로젝트 |
| 🥈 2     | **Tortoise ORM** | FastAPI 특화, 간단한 문법     | ✅ (aerich 사용)   | ✅ 완전 지원      | ✅ 중소형 프로젝트 |
| 🥉 3     | **Gino**         | PostgreSQL 전용, 고성능       | ❌ (Alembic X)     | ✅ 완전 지원      | ⚠️ Postgres 한정  |
| ❌ 제외 | Peewee / Pony     | 경량, 학습용                  | ❌                 | ❌                | ❌ FastAPI 부적합 |

---

## ✅ 선택 기준 요약

- **SQLAlchemy**: 실무 표준, 확장성 최고, Alembic으로 마이그레이션 완벽 지원
- **Tortoise ORM**: 간편하고 빠르며 FastAPI에 최적화된 비동기 ORM
- **Gino**: PostgreSQL 환경에서 고성능 API 개발 시 적합 (Postgres only)
- **Peewee / Pony**: 비동기 미지원, 실무용 FastAPI 프로젝트에 비추천

---

## 🔚 권장 조합

> **SQLAlchemy + Alembic + FastAPI + Pydantic**

: 가장 실전적이고 안정적인 ORM 스택 구성