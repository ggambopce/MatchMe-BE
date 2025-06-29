import strawberry
from graphql_router.profile.types import (
    ProfileInput,
    ContactProfileInput,
    UserChoiceInput,
    CreateProfileResponse
)
from graphql_router.profile.resolver import ProfileResolver

@strawberry.type
class ProfileMutation:
    @strawberry.mutation
    async def create_profile(
        user_id: str,
        profile: ProfileInput,
        contact_profile: ContactProfileInput | None = None,
        user_choice_list: list[UserChoiceInput] = []
    ) -> CreateProfileResponse:
        result = await ProfileResolver.create_profile(
            user_id=user_id,
            profile=profile,
            contact=contact_profile,
            choices=user_choice_list
        )
        return CreateProfileResponse(**result)
