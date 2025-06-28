import strawberry
from datetime import datetime

#uuid 작성
@strawberry.input
class UserInput:
    user_id: str
    created_at: datetime

@strawberry.type
class UserType:
    user_id: str
    created_at: datetime
