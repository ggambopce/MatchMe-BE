# MatchMe-BE

## 설치 패키지 목록
- fastapi 
- strawberry-graphql 
- uvicorn 
- websockets
- tortoise-orm[asyncpg]
- apscheduler

## uv 사용 방법
### 메뉴얼 
- https://docs.astral.sh/uv/ [메뉴얼]
- https://docs.astral.sh/uv/#installation [설치 방법]

### 패키지 추가
```bash
uv add <패키지명>
```
### requirements.txt 생성
```bash
uv pip freeze > requirements.txt
```

### 프로그램 실행
```bash
uv run ./src/main.py
````

## FastAPI

### 테스트 페이지
- http://127.0.0.1:7070/docs
- http://127.0.0.1:7070/redoc

## GraphQL
### GraphQL Playground
- http://127.0.0.1:7070/graphql

## 도커
- 현재 데이터베이스만 구축 / postgres:15
### Docker Compose 실행
```bash
# 데이터베이스 컨테이너 실행
docker compose up -d 
 # 데이터베이스 컨테이너 중지
docker compose down
```
### 접속 정보
- 호스트: localhost
- 포트: 5432
- 데이터베이스: matchme
- 사용자: app
- 비밀번호: 1234