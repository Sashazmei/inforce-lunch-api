from django.urls import path
from .views import (
    MenuListCreateView,
    TodayMenuView,
    EmployeeChoiceCreateView,
    TodayResultsView
)

urlpatterns = [
    path("", MenuListCreateView.as_view()),
    path("today/", TodayMenuView.as_view()),
    path("choice/", EmployeeChoiceCreateView.as_view()),
    path("today/results/", TodayResultsView.as_view()),
]
