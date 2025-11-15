from django.contrib import admin
from .models import Menu, EmployeeChoice


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "restaurant", "date")
    list_filter = ("date", "restaurant")
    search_fields = ("restaurant__name",)


@admin.register(EmployeeChoice)
class EmployeeChoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "menu", "selected_item", "created_at")
    list_filter = ("menu", "employee")
    search_fields = ("employee__username", "selected_item")
