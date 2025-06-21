from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.CharField(max_length=128, pk=True)
    username = fields.CharField(max_length=50, unique=False)
    email = fields.CharField(max_length=100, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)