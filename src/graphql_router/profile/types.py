
import strawberry

# GraphQL에 노출될 객체들의 타입 정의
# 클라이언트에 보여줄 데이터 구조 정의
# Response DTO 같은 역할
# 내부 Pydantic Model 또는 DB 모델을 이 타입으로 변환해 반환 

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
    
# 매칭 프로필 조회 타입 (이성프로필)
@strawberry.type
class MatchProfileResponse:
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
    match_score: int
    match_report: str

# 쌍방 수락 시 프로필 추가 정보 조회(연락처 정보)
@strawberry.type
class ContactProfileResponse:
    phone_number: str
    sns_url: str
