import strawberry
from datetime import date
import random

from graphql_router.profile.types import UserChoiceInput
from graphql_router.match.service import MatchService
from db.profile.models import Profile, UserChoice
from db.match.models import MatchProfile
from graphql_router.match.dataclass import MatchProfileData



@strawberry.type
class MatchMutation:

    @strawberry.mutation
    async def create_match_profiles(self) -> str:
        # 1. 모든 남녀 유저 조회
        males = await Profile.filter(gender="male").all()
        females = await Profile.filter(gender="female").all()

        if not males or not females:
            return "매칭 가능한 남녀 유저가 부족합니다."

        # 2. 무작위 순서로 섞기
        random.shuffle(males)
        random.shuffle(females)

        # 3. 남녀 중 수가 적은 쪽 기준으로 페어 생성
        num_pairs = min(len(males), len(females))
        pairs = zip(males[:num_pairs], females[:num_pairs])

        # 4. 매칭 수행
        for user1, user2 in pairs:
            user1_raw_choices = await UserChoice.filter(profile=user1).all()
            user2_raw_choices = await UserChoice.filter(profile=user2).all()

            user1_choices = [
                UserChoiceInput(question_number=c.question_number, choice_number=c.choice_number)
                for c in user1_raw_choices
            ]
            user2_choices = [
                UserChoiceInput(question_number=c.question_number, choice_number=c.choice_number)
                for c in user2_raw_choices
            ]

            match_result: MatchProfileData = await MatchService.set_match_score_match_report(
                user1_choices, user2_choices,
                user1, user2
            )

            for u1, u2 in [(user1, user2), (user2, user1)]:
                await MatchProfile.create(
                    user=u1,
                    matched_user_id=u2.id,
                    nickname=u2.nickname,
                    temperament=u2.temperament,
                    enneagram=u2.enneagram,
                    introduction=u2.introduction,
                    gender=u2.gender,
                    birth_date=u2.birth_date,
                    job=u2.job,
                    profile_image_url=u2.profile_image_url,
                    location=u2.location,
                    relationship_intent=u2.relationship_intent,
                    temperament_report=u2.temperament_report,
                    match_score=match_result.match_score,
                    match_report=match_result.match_report
                )

        return f"{num_pairs}쌍 매칭 성공"

