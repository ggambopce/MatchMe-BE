import strawberry
from graphql_router.profile.types import ProfileType
from graphql_router.profile.resolver import ProfileResolver


# GrapgQL 진입점
# 비동기적으로 DB에서 프로필을 조회하고, 그 결과를 ProfileType으로 반환하는 Query 진입점 정의
@strawberry.type
class Query:
    @strawberry.field
    async def get_profile(self, user_id: str) -> ProfileType:
        result = await ProfileResolver.get_profile(user_id)
        return result
    
    @strawberry.field
    def ping(self) -> str:
        return "pong"
