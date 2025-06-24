# graphql_router/profile/types.py
import strawberry

@strawberry.input
class ProfileInput:
    nickname: str
    introduction: str
    birth_date: str
    gender: str
    job: str
    profile_image_url: str
    location: str
    relationship_intent: str

@strawberry.input
class ContactProfileInput:
    phone_number: str | None = None
    sns_url: str | None = None

@strawberry.input
class UserChoiceInput:
    question_number: int
    choice_number: int

@strawberry.type
class CreateProfileResponse:
    code: str
    message: str
