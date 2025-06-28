import strawberry
from graphql_router.profile.types import MatchProfileResponse
from db.match.models import MatchProfile

@strawberry.type
class MatchQuery:
    
    @strawberry.field
    async def get_my_match_profiles(self, user_id: int) -> list[MatchProfileResponse]:
        matches = await MatchProfile.filter(user_id=user_id).all()
        return [
            MatchProfileResponse(
                profile_id=m.id,
                nickname=m.nickname,
                temperament=m.temperament,
                enneagram=m.enneagram,
                introduction=m.introduction,
                gender=m.gender,
                age=m.age,
                job=m.job,
                profile_image_url=m.profile_image_url,
                location=m.location,
                relationship_intent=m.relationship_intent,
                temperament_report=m.temperament_report,
                match_score=m.match_score,
                match_report=m.match_report,
            )
            for m in matches
        ]

