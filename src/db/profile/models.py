from tortoise import fields
from tortoise.models import Model

# DB 모델 또는 ORM 객체 정의 (Tortoise ORM)
# DB 테이블과 매핑되는 클래스
# 실제 데이터를 저장하거나 가져오는 역할
class Profile(Model):
    id = fields.IntField(pk=True)

    # 관계
    user = fields.ForeignKeyField("models.User", related_name="profile", on_delete=fields.CASCADE)

    # 공통 필드
    nickname = fields.CharField(max_length=50)
    introduction = fields.TextField()
    birth_date = fields.CharField(max_length=20)
    gender = fields.CharField(max_length=10)
    job = fields.CharField(max_length=50)
    profile_image_url = fields.CharField(max_length=200)
    location = fields.CharField(max_length=100)
    relationship_intent = fields.CharField(max_length=100)

    # 조회 시 필요한 추가 필드
    temperament = fields.CharField(max_length=50, null=True)
    enneagram = fields.CharField(max_length=50, null=True)
    temperament_report = fields.TextField(null=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "profile"


class ContactProfile(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="contact_profile", on_delete=fields.CASCADE)

    phone_number = fields.CharField(max_length=20, null=True)
    sns_url = fields.CharField(max_length=200, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "contact_profile"

class UserChoice(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_choices", on_delete=fields.CASCADE)

    question_number = fields.IntField()
    choice_number = fields.IntField()

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_choice"

