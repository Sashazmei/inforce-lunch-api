from django.urls import path
from .views import RegisterView, UsersListView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("", UsersListView.as_view()),
]
