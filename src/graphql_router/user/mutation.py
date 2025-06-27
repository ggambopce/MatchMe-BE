import strawberry
from datetime import datetime
from src.db.user.models import User
from src.graphql_router.user.types import UserType

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_user(self, device_id: str, name: str = "비회원") -> UserType:
        user = await User.get_or_none(id=device_id)

        if user:
            return UserType(
                id=user.id,
                name=user.name,
                created_at=user.created_at
            )

        new_user = await User.create(id=device_id, name=name)
        return UserType(
            id=new_user.id,
            name=new_user.name,
            created_at=new_user.created_at
        )
