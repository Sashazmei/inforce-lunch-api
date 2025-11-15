from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    """
    Разрешает доступ только пользователям, у которых is_employee=True.
    """
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.is_employee)
