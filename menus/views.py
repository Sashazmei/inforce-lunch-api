from datetime import date
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Menu, EmployeeChoice
from .serializers import MenuSerializer, EmployeeChoiceSerializer
from .permissions import IsEmployee


class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class TodayMenuView(generics.RetrieveAPIView):
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]   # меню на сегодня можно смотреть всем

    def get_object(self):
        today = date.today()
        try:
            return Menu.objects.get(date=today)
        except Menu.DoesNotExist:
            raise NotFound("Menu for today does not exist.")


class EmployeeChoiceCreateView(generics.CreateAPIView):
    queryset = EmployeeChoice.objects.all()
    serializer_class = EmployeeChoiceSerializer
    permission_classes = [IsEmployee]


class TodayResultsView(generics.ListAPIView):
    serializer_class = EmployeeChoiceSerializer
    permission_classes = [IsEmployee]

    def get_queryset(self):
        try:
            today_menu = Menu.objects.get(date=date.today())
        except Menu.DoesNotExist:
            raise NotFound("Menu for today does not exist.")
        return EmployeeChoice.objects.filter(menu=today_menu)
