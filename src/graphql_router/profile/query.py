import strawberry
from graphql_router.profile.types import ProfileType
from graphql_router.profile.resolver import ProfileResolver
from graphql_router.profile.types import MatchProfileResponse


# 클라이언트가 요청할 수 있는 조회용 기능(Query) 를 정의
# 내부적으로 서비스 호출 → DB 조회 → 타입으로 변환 → 반환
# GrapgQL 진입점
# 비동기적으로 DB에서 프로필을 조회하고, 그 결과를 ProfileType으로 반환하는 Query 진입점 정의
@strawberry.type
class Query:
    # 내 프로필 조회
    @strawberry.field
    async def get_profile(self, user_id: str) -> ProfileType:
        result = await ProfileResolver.get_profile(user_id)
        return result
    # 매칭 프로필 조회
    @strawberry.field
    async def get_match_profile(self, user_id: str) -> MatchProfileResponse:
        return await ProfileResolver.get_match_profile(user_id)
    
    @strawberry.field
    def ping(self) -> str:
        return "pong"

