from django.db import models
from django.conf import settings


class Restaurant(models.Model):
    """
    Ресторан. Предполагаем, что у ресторана есть владелец (User).
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="restaurants",
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
