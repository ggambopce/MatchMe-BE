from tortoise import fields
from tortoise.models import Model
import uuid

class User(Model):
    user_id = fields.CharField(pk=True, max_length=128, default=lambda: str(uuid.uuid4()))
    created_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        table = "user"