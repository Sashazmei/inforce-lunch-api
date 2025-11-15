from rest_framework import serializers
from .models import Menu, EmployeeChoice


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "restaurant", "date", "items"]
        read_only_fields = ["id"]


class EmployeeChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeChoice
        fields = ["id", "employee", "menu", "selected_item", "created_at"]
        read_only_fields = ["id", "employee", "created_at"]

    def create(self, validated_data):
        validated_data["employee"] = self.context["request"].user
        return super().create(validated_data)
