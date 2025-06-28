# graphql_router/resolvers/profile_resolver.py

from db.profile.models import  Profile, ContactProfile, UserChoice
from src.db.user.models import User
from db.match.models import MatchResult
from graphql_router.profile.types import ProfileInput, ContactProfileInput, UserChoiceInput, ProfileType, ContactProfileType, MatchProfileResponse, ContactProfileResponse
from tortoise.exceptions import DoesNotExist

# Query나 Mutation에서 호출되는 비즈니스 로직 담당 계층
# DB 접근, 데이터 가공, 외부 API 호출 등 포함
# 복잡한 로직은 이 계층에서 처리하고 결과만 Query에 넘김

class ProfileResolver:

    # 내 프로필 작성 리졸버
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

# 내 프로필 조회 리졸버
    @staticmethod
    async def get_profile(user_id: str) -> ProfileType:
        profile = await Profile.get(user__id=user_id).prefetch_related("user")
        contact_profile = await ContactProfile.filter(user=profile.user).first()
        
        contact_profile_data = None
        if contact_profile:
            contact_profile_data = ContactProfileType(
                phone_number=contact_profile.phone_number,
                sns_url=contact_profile.sns_url
            )
        
        return ProfileType(
            profile_id=profile.id,
            nickname=profile.nickname,
            temperament=profile.temperament,
            enneagram=profile.enneagram,
            introduction=profile.introduction,
            age=profile.birth_date,
            job=profile.job,
            profile_image_url=profile.profile_image_url,
            location=profile.location,
            relationship_intent=profile.relationship_intent,
            temperament_report=profile.temperament_report,
            contact_profile=contact_profile_data
        )    
    
# 매칭 프로필 조회 리졸버
    @staticmethod
    async def get_match_profile(user_id: str) -> MatchProfileResponse:
        try:
            # 1. 현재 유저와 매칭된 이성 프로필 조회 (가장 최근 1건)
            match = await MatchInfo.get(user__id=user_id).prefetch_related("matched_profile")

            # 2. 매칭된 이성 프로필 정보 가져오기
            profile = await Profile.get(id=match.matched_profile.id)

            return MatchProfileResponse(
                profile_id=profile.id,
                nickname=profile.nickname,
                temperament=profile.temperament,
                enneagram=profile.enneagram,
                introduction=profile.introduction,
                age=profile.birth_date,
                job=profile.job,
                profile_image_url=profile.profile_image_url,
                location=profile.location,
                relationship_intent=profile.relationship_intent,
                temperament_report=profile.temperament_report,
                match_score=match.match_score,
                match_report=match.match_report
            )

        except DoesNotExist:
            raise Exception("매칭된 프로필이 존재하지 않습니다.")

# 쌍방 수락 시 프로필 추가 정보 조회
    @staticmethod
    async def get_matched_contact_profile(user_id: str) -> ContactProfileResponse:
        try:
            # 1. 매칭 정보 조회
            match = await MatchInfo.get(user__id=user_id).prefetch_related("matched_profile")

            # 2. 쌍방 수락 여부 확인 (예시 플래그: is_accepted_by_both)
            if not match.is_accepted_by_both:
                raise Exception("아직 쌍방 수락되지 않았습니다.")

            # 3. 매칭된 상대의 연락처 정보 가져오기
            contact = await ContactProfile.get(user=match.matched_profile.user)

            return ContactProfileResponse(
                phone_number=contact.phone_number,
                sns_url=contact.sns_url
            )

        except DoesNotExist:
            raise Exception("연락처 정보를 찾을 수 없습니다.")         