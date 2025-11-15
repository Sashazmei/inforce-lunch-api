from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_employee"]
        read_only_fields = ["id"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "is_employee"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data.get("email"),
            is_employee=validated_data.get("is_employee", False)
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
