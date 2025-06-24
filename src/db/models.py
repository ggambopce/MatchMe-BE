from tortoise import fields
from tortoise.models import Model
import uuid

class User(Model):
    id = fields.CharField(pk=True, max_length=128, default=lambda: str(uuid.uuid4()))
    name = fields.CharField(max_length=50, unique=False, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "user"