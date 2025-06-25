
import strawberry

# 프로필 작성 타입
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

# 내 프로필 조회 타입
@strawberry.type
class ContactProfileType:
    phone_number: str | None = None
    sns_url: str | None = None
@strawberry.type
class ProfileType:
    profile_id: int
    nickname: str
    temperament: str
    enneagram: str
    introduction: str
    age: str
    job: str
    profile_image_url: str
    location: str
    relationship_intent: str
    temperament_report: str
    contact_profile: ContactProfileType
    

