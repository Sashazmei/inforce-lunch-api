from django.db import models
from restaurants.models import Restaurant
from django.conf import settings


class Menu(models.Model):
    """
    Меню ресторана на конкретный день.
    items — список блюд (простая JSON-структура)
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menus",
    )
    date = models.DateField()
    items = models.JSONField(help_text="List of dishes for this day")

    class Meta:
        unique_together = ("restaurant", "date")
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"{self.restaurant.name} - {self.date}"


class EmployeeChoice(models.Model):
    """
    Выбор сотрудника на конкретное меню.
    employee — пользователь с is_employee=True
    selected_item — текст выбранного блюда (одно из items)
    """
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="menu_choices",
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="choices",
    )
    selected_item = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "menu")

    def __str__(self) -> str:
        return f"{self.employee.username} -> {self.menu}"
