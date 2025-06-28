
from graphql_router.match.types import MatchResultType, AcceptStatus
from graphql_router.profile.types import ProfileType
from graphql_router.match.service import MatchService

import strawberry
from typing import List

@strawberry.type
class Query:
    
    @strawberry.field
    async def get_my_match_result(self, user_id: str) -> MatchResultType:
        return await MatchService.get_my_match_result(user_id)

