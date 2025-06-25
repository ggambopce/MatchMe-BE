from fastapi import FastAPI

from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from scheduler import job

from tortoise.contrib.fastapi import register_tortoise

from graphql_router import graphql
from fastapi_router import test

# 주기적으로 실행할 작업 정의
scheduler = BackgroundScheduler()
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 앱 시작 시 실행
    #scheduler.add_job(job.schedule_job, 'cron', minute=0)  # 매 시간 정각에 실행
    scheduler.add_job(job.schedule_job, IntervalTrigger(seconds=10), replace_existing=True)  # 10초마다 실행
    scheduler.start()
    yield
    # 앱 종료 시 실행
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

register_tortoise(
    app,
    db_url="postgres://app:1234@localhost:5432/matchme",  # 또는 PostgreSQL URL
    modules={"models": ["db.models"]},  # 경로 주의
    generate_schemas=True,
    add_exception_handlers=True
)

# 라우터 등록
app.include_router(graphql.graphql_app, prefix="/graphql")
app.include_router(test.router, prefix="/api")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=7070, reload=True)