from fastapi import APIRouter
from db import models
import uuid

router = APIRouter(
    prefix="/tests",       # URL prefix
    tags=["test"],        # 문서화 태그
)

@router.get("/01")
async def test_01():
    await models.User.create(
        id=uuid.uuid4(),
        username="이준식",
        email=""
    );

    return await models.User.all();