# graphql_router/resolvers/profile_resolver.py

from db.profile.models import  Profile, ContactProfile, UserChoice
from db.models import User
from graphql_router.profile.types import ProfileInput, ContactProfileInput, UserChoiceInput

class ProfileResolver:

    @staticmethod
    async def create_profile(user_id: str, profile: ProfileInput, contact: ContactProfileInput | None, choices: list[UserChoiceInput]):
        user = await User.get_or_none(id=user_id)
        if not user:
            return {"code": "ER", "message": "사용자를 찾을 수 없습니다."}

        # 이미 프로필이 있는 경우 처리 (예: 업데이트 or 무시)
        existing = await Profile.get_or_none(user=user)
        if existing:
            return {"code": "ALREADY_EXISTS", "message": "이미 프로필이 존재합니다."}

        # 프로필 저장
        await Profile.create(user=user, **profile.__dict__)

        # 연락처 저장 (optional)
        if contact:
            await ContactProfile.create(user=user, **contact.__dict__)

        # 설문 응답 저장
        for choice in choices:
            await UserChoice.create(user=user, question_number=choice.question_number, choice_number=choice.choice_number)

        return {"code": "SU", "message": "프로필이 성공적으로 생성되었습니다."}
