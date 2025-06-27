import strawberry
from datetime import datetime

@strawberry.type
class UserType:
    id: str
    name: str | None
    created_at: datetime
