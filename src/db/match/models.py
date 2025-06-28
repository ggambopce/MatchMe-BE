# db/models/match.py

from tortoise import fields
from tortoise.models import Model


class MatchResult(Model):
    match_result_id = fields.IntField(pk=True)

    # 프로필 1
    profile1 = fields.ForeignKeyField(
        "models.Profile", related_name="match_results_as_profile1", on_delete=fields.CASCADE
    )
    # 프로필 2
    profile2 = fields.ForeignKeyField(
        "models.Profile", related_name="match_results_as_profile2", on_delete=fields.CASCADE
    )

    # 점수 및 보고서
    match_score = fields.IntField()
    match_report = fields.TextField()

    # 수락 상태 (WAITING, ACCEPTED, REJECTED)
    accept_status = fields.CharField(max_length=20, default="WAITING")

    # 타임스탬프
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "match_result"
        unique_together = (("profile1", "profile2"),)
        
        
# 매치 프로필 (이성 프로필)
class MatchProfile(Model):
    id = fields.IntField(pk=True)  # profile_id 대응
    
    # 나 자신
    user = fields.ForeignKeyField("models.Profile", related_name="match_profile")      
    
    # 상대방 정보
    matched_user_id = fields.IntField()  # matched_user와 연결해도 되지만, 삭제될 수도 있으므로 ID만 저장
    nickname = fields.CharField(max_length=50)
    temperament = fields.CharField(max_length=30)
    enneagram = fields.CharField(max_length=30)
    introduction = fields.TextField()
    gender = fields.CharField(max_length=10)
    age = fields.CharField(max_length=10)
    job = fields.CharField(max_length=50)
    profile_image_url = fields.CharField(max_length=255)
    location = fields.CharField(max_length=100)
    relationship_intent = fields.CharField(max_length=100)
    temperament_report = fields.TextField()
    
    #매칭 정보
    match_score = fields.IntField()
    match_report = fields.TextField()
    
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "match_profile"        