from django.db import models
import uuid

# Create your models here.
class User_data(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(blank = True, max_length = 255)
    last_name = models.CharField(blank = True, max_length = 255)
    user_email = models.CharField(blank = True, max_length = 255)
    user_number = models.CharField(blank = True, max_length = 10)
    auth_id = models.CharField(blank = True, max_length = 255)

    def __str__(self) -> str:
        return self.first_name
