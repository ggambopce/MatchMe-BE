import strawberry
from datetime import date
import random

from graphql_router.profile.types import UserChoiceInput
from graphql_router.match.service import MatchService
from db.profile.models import Profile, UserChoice
from db.match.models import MatchProfile


@strawberry.type
class MatchMutation:

    @strawberry.mutation
    async def create_match_profiles(self) -> str:
        # 1. 오늘 매칭되지 않은 유저 필터링
        matched_ids = await MatchProfile.filter(
            created_at__date=date.today()
        ).values_list("user_id", flat=True)

        males = await Profile.exclude(id__in=matched_ids).filter(gender="male").all()
        females = await Profile.exclude(id__in=matched_ids).filter(gender="female").all()

        if not males or not females:
            return "매칭 가능한 남녀 유저가 부족합니다."

        # 2. 무작위 선택
        user1 = random.choice(males)
        user2 = random.choice(females)

        # 3. 선택지 가져오기
        user1_raw_choices = await UserChoice.filter(user_id=user1.id).all()
        user2_raw_choices = await UserChoice.filter(user_id=user2.id).all()

        user1_choices = [
            UserChoiceInput(question_number=c.question_number, choice_number=c.choice_number)
            for c in user1_raw_choices
        ]
        user2_choices = [
            UserChoiceInput(question_number=c.question_number, choice_number=c.choice_number)
            for c in user2_raw_choices
        ]

        # 4. 점수 및 매칭 리포트 계산
        match_result = await MatchService.set_match_score_match_report(
            user1_choices, user2_choices,
            user1.gender, user2.gender
        )

        # 5. 양방향 MatchProfile 저장
        for u1, u2 in [(user1, user2), (user2, user1)]:
            await MatchProfile.create(
                user=u1,
                matched_user_id=u2.id,
                nickname=u2.nickname,
                temperament=u2.temperament,
                enneagram=u2.enneagram,
                introduction=u2.introduction,
                gender=u2.gender,
                age=u2.age,
                job=u2.job,
                profile_image_url=u2.profile_image_url,
                location=u2.location,
                relationship_intent=u2.relationship_intent,
                temperament_report=u2.temperament_report,
                match_score=match_result.match_score,
                match_report=match_result.match_report
            )

        return "매칭 성공"
