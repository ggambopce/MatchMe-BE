from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise
from graphql_router.schema import graphql_app


app = FastAPI()

register_tortoise(
    app,
    db_url="postgres://app:1234@localhost:5432/matchme",  # 또는 PostgreSQL URL
    modules={"models": ["db.user.models","db.profile.models","db.match.models"]},  # 경로 주의
    generate_schemas=True,
    add_exception_handlers=True
)

app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=7070, reload=True)