from tortoise import fields
from tortoise.models import Model

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
