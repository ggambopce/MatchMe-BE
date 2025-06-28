# src/graphql_router/user/resolver.py

from src.db.user.models import User
from src.graphql_router.user.types import UserType

class UserResolver:

    @staticmethod
    async def add_user(user_id: str, created_at: datetime) -> UserType:
        # 이미 존재하는지 확인
        user = await User.get_or_none(user_id=user_id)
        if user:
            return UserType(user_id=user.user_id, created_at=user.created_at)

        # 없으면 생성
        new_user = await User.create(user_id=user_id, created_at=created_at)
        return UserType(user_id=new_user.user_id, created_at=new_user.created_at)