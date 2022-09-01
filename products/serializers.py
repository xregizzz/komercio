from asyncore import read
from rest_framework import serializers
from .models import Product
from accounts.serializers import AccountSerializer


class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = [
            "seller",
        ]


class PostProductSerializer(serializers.ModelSerializer):
    seller = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "description",
            "price",
            "quantity",
            "is_active",
            "seller",
        ]
        read_only_fields = ["is_active"]
