from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/login/", obtain_auth_token),   # ← логин, возвращает токен
    path("api/users/", include("users.urls")),
    path("api/restaurants/", include("restaurants.urls")),
    path("api/menus/", include("menus.urls")),
]
