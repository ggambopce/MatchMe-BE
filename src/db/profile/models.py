from tortoise import fields
from tortoise.models import Model

# 내 프로필 작성 model
class Profile(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="profile", on_delete=fields.CASCADE)
    
    nickname = fields.CharField(max_length=50)
    introduction = fields.TextField()
    birth_date = fields.CharField(max_length=20)
    gender = fields.CharField(max_length=10)
    job = fields.CharField(max_length=50)
    profile_image_url = fields.CharField(max_length=200)
    location = fields.CharField(max_length=100)
    relationship_intent = fields.CharField(max_length=100)

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

# 내 프로필 조회 모델
class Profile(Model):
    id = fields.IntField(pk=True)

    nickname = fields.CharField(max_length=50)
    temperament = fields.CharField(max_length=50)
    enneagram = fields.CharField(max_length=50)
    introduction = fields.TextField()
    birth_date = fields.CharField(max_length=20)
    job = fields.CharField(max_length=50)
    profile_image_url = fields.CharField(max_length=200)
    location = fields.CharField(max_length=100)
    relationship_intent = fields.CharField(max_length=100)
    temperament_report = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    user = fields.ForeignKeyField("models.User", related_name="profile")

    class Meta:
        table = "profile"
        
        