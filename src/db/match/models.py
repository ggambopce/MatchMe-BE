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