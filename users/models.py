from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Расширенный пользователь.
    is_employee = True  -> пользователь является сотрудником компании
    is_employee = False -> обычный пользователь (например, владелец ресторана, админ и т.п.)
    """
    is_employee = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username
