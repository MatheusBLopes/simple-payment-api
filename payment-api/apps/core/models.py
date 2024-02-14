# myapp/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # add custom fields if needed
    pass
