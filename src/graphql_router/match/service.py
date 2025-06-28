# graphql_router/match/service.py

from typing import List
from graphql_router.match.types import MatchResultType

class MatchService:
    
    # 메인 매칭 로직
    @staticmethod
    async def matching(user_id: str) -> MatchResultType:
        """
        매칭 로직을 정의한다.
        """
        # TODO: 
        # TODO: 
        # TODO: 각 결과를 MatchProfileResponse과 MatchResultType에 반영

        # 예시 반환
        return None

    # 관리자용 결과 내용 조회
    @staticmethod
    async def get_my_match_result(user_id: str) -> MatchResultType:
        """
        주어진 user_id를 기준으로, 관련된 match_result들을 조회하여
        MatchResultType 리스트로 반환한다.
        """
        # TODO: user_id로 profile 조회
        # TODO: profile1_id 또는 profile2_id에 해당하는 match_result 검색
        # TODO: 각 결과를 MatchResultType으로 매핑

        # 예시 반환
        return None

