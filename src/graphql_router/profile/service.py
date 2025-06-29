from graphql_router.profile.dataclass import ProfileServiceResponse
from graphql_router.profile.enum import TEMPERAMENT_MAP, ENNEAGRAM_MAP, TEMPERAMENT_REPORT_MAP

class ProfileService:
     
    # 설문지 입력값 기반 가공 후 변수에 저장 
    # 1번에서 temperament 결정
    # 2번에서 에니어그램 유형 결정
    # 프로필 작성을 위해서 우선 2개만 결정
    @staticmethod
    async def setMyPofile(user_choice_list: list[dict]) -> ProfileServiceResponse:
        temperament = None
        enneagram = None

        # 설문 응답 순회하며 필요한 항목 추출
        for choice in user_choice_list:
            qn = choice["question_number"]
            cn = choice["choice_number"]

            if qn == 1:  # 기질 결정
                temperament = TEMPERAMENT_MAP.get(cn)
                temperament_report = TEMPERAMENT_REPORT_MAP.get(temperament)
            elif qn == 2:  # 에니어그램 결정
                enneagram = ENNEAGRAM_MAP.get(cn)

        # 결과를 ProfileType에 매핑
        return ProfileServiceResponse(
            temperament=temperament,
            enneagram=enneagram,
            temperament_report=temperament_report
        )