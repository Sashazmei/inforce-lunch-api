from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("username", "email", "is_staff", "is_employee", "is_active")
    list_filter = ("is_staff", "is_employee", "is_active")
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Employee info", {"fields": ("is_employee",)}),
    )
