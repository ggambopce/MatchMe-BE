import strawberry
from datetime import datetime
from src.db.user.models import User
from src.graphql_router.user.types import UserInput, UserType
from src.graphql_router.user.resolver import UserResolver

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_user(self, input: UserInput) -> UserType:
        return await UserResolver.add_user(
            user_id=input.user_id,
            created_at=input.created_at
        )
