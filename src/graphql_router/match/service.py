from random import random

from graphql_router.profile.types import MatchProfileResponse
from graphql_router.match.types import MatchResultType
from graphql_router.match.enum import TEMPERAMENT_PAIR_REPORT_MAP
from graphql_router.profile.enum import TEMPERAMENT_MAP, ENNEAGRAM_MAP
from graphql_router.profile.types import UserChoiceInput


class MatchService:
    
    # 매치 기준 : 성별 랜던 매칭
    @staticmethod
    async def match_two_profiles() -> MatchProfileResponse:
        males = await MatchProfileResponse.filter(gender="male")
        females = await MatchProfileResponse.filter(gender="female")

        if not males or not females:
            raise Exception("성별이 다른 프로필이 필요합니다.")

        return random.profile_id(males), random.profile_id(females)



    # 매치 스코어와 매치리포트 생성 메서드
    @staticmethod
    async def set_match_score_match_report(
        user1_choices: list[UserChoiceInput],
        user2_choices: list[UserChoiceInput]
        ) -> MatchProfileResponse:
        # 선택값 딕셔너리로 정리
        u1 = {c.question_number: c.choice_number for c in user1_choices}
        u2 = {c.question_number: c.choice_number for c in user2_choices}
        
        score = 0

        '''Temperament 기질(Q1)
        25점인 경우
        1번-1번, 2번-2번, 3번-4번, 4번-3번
        나머지 쌍은 20점
        '''
        t1 = TEMPERAMENT_MAP.get(u1[1])
        t2 = TEMPERAMENT_MAP.get(u2[1])
        if t1 == t2 or (u1[1], u2[1]) in [(3, 4), (4, 3)]:
            score += 25
        else:
            score += 20

        match_report = TEMPERAMENT_PAIR_REPORT_MAP.get((t1, t2)) or TEMPERAMENT_PAIR_REPORT_MAP.get((t2, t1)) or "기질 궁합 리포트 없음"

        ''' Enneagram 애니어그램(Q2)
        25점인 경우 - 합쳐서 10인 경우 
        1번-9번/2번-8번/...5번-5번/...../9번-1번
        나머지 쌍은 20점
        '''
        e1 = u1[2]
        e2 = u2[2]
        score += 25 if (e1 + e2 == 10) else 20

        ''' Maturity 성숙도 (Q3)
        25점인 경우
        1-1/2-2/3-3 같은 수준끼리 만났을 때.
        20점인 경우
        1-2/2-3/2-1/3-2 한 단계씩 차이나게 만났을 때
        15점인 경우 
        1-3/3-1 두 단계씩 차이나게 만났을 때
        '''
        m1 = u1[3]
        m2 = u2[3]
        diff = abs(m1 - m2)
        if diff == 0:
            score += 25
        elif diff == 1:
            score += 20
        else:
            score += 15

        '''Instinct 본능 (Q4)
        25점인 경우 
        1-1/2-2/3-3 같게 만났을 때
        20점인 경우
        1-2/1-3/2-1/3-1만났을 때
        15점인 경우
        나머지
        '''
        i1 = u1[4]
        i2 = u2[4]
        if i1 == i2:
            score += 25
        elif (i1 == 1 and i2 in [2, 3]) or (i2 == 1 and i1 in [2, 3]):
            score += 20
        else:
            score += 15

        return MatchProfileResponse(
            match_score=score,
            match_report=match_report
        )