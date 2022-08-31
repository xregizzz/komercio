from rest_framework.views import APIView, Request, Response, status
from .serializers import LoginSerializer, AccountSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .models import Account


# Create your views here.
class AccountLogin(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response({"detail": "invalid username or password"})

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailsView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        max_accounts = self.kwargs["num"]
        return self.queryset.order_by("-date_joined")[0:max_accounts]
