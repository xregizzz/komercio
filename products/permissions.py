from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Product


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method == "GET":
            return True

        return request.user.is_seller


class IsProductOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, product: Product):

        if request.user == product.seller:
            return True

        else:
            return False
