from fastapi import APIRouter
from pydantic import BaseModel
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
        name="김혜인",
    );

    return await models.User.all();

class UserCreateRequest(BaseModel):
    device_id: str

@router.post("/users")
async def register_user(req: UserCreateRequest):
    user = await models.User.get_or_none(id=req.device_id)
    if user:
        return user
    return await models.User.create(id=req.device_id, name="비회원")