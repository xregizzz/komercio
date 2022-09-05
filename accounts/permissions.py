from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Account


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user == Account.objects.get(pk=view.kwargs["pk"])
