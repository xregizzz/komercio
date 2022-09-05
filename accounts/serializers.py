from rest_framework import serializers
from .models import Account


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class AccountSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_seller",
            "password",
            "is_active",
            "is_superuser",
            "date_joined",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Account:
        user = Account.objects.create_user(**validated_data)

        return user


class AccountSerializerManagement(AccountSerializer):
    is_active = serializers.BooleanField()
