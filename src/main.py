import asyncio
import datetime
from typing import AsyncGenerator
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Service:
    name: str
    status: str
    description: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@strawberry.type
class User:
    name: str
    status: str
    services: list[Service]


# 임시 데이터 저장소
users_data = [
    User(
        name="User A",
        status="active",
        services=[
            Service(
                name="Service A1",
                status="running",
                description="Service A1 description",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            Service(
                name="Service A2",
                status="stopped",
                description="Service A2 description",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
        ],
    ),
    User(
        name="User B",
        status="inactive",
        services=[
            Service(
                name="Service B1",
                status="running",
                description="Service B1 description",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            Service(
                name="Service B2",
                status="stopped",
                description="Service B2 description",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
        ],
    ),
    User(
        name="User C",
        status="active",
        services=[
            Service(
                name="Service C1",
                status="running",
                description="Service C1 description",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
            Service(
                name="Service C2",
                status="stopped",
                description="Service C2 description",
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            ),
        ],
    ),
]


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return users_data

    @strawberry.field
    def services(self, user_name: str) -> list[Service]:
        for user in users_data:
            if user.name == user_name:
                return user.services
        raise ValueError(f"User with name {user_name} not found")


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_service(
        self, user_name: str, service_name: str, status: str, description: str
    ) -> Service:
        for user in users_data:
            if user.name == user_name:
                new_service = Service(
                    name=service_name,
                    status=status,
                    description=description,
                    created_at=datetime.datetime.now(),
                    updated_at=datetime.datetime.now(),
                )
                user.services.append(new_service)
                return new_service
        raise ValueError(f"User with name {user_name} not found")

    @strawberry.mutation
    def add_user(self, name: str, status: str) -> User:
        if any(user.name == name for user in users_data):
            raise ValueError(f"User with name {name} already exists")
        new_user = User(name=name, status=status, services=[])
        users_data.append(new_user)
        return new_user


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def user_status_updates(self) -> AsyncGenerator[User, None]:
        while True:
            await asyncio.sleep(1)
            for user in users_data:
                await asyncio.sleep(1)
                yield user


schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=7070, reload=True)