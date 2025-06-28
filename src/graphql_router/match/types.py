import strawberry

from graphql_router.profile.types import ProfileType


@strawberry.type
class MatchResultType:
    match_result_id: int        
    match_score: int
    match_maturity: str
    match_instinct: str
    match_report: str
    accept_status: str      # 수락상태 enum 변경 예정
    profile1: ProfileType
    profile2: ProfileType
