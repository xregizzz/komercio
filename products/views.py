from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .models import Product
from .serializers import GetProductSerializer, PostProductSerializer
from .permissions import IsSellerOrReadOnly, IsProductOwner


class SerializerByMethodMixin:
    def get_serializer_class(self):
        return self.serializer_map.get(self.request.method)


class ProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerOrReadOnly]

    queryset = Product.objects.all()

    serializer_map = {
        "GET": GetProductSerializer,
        "POST": PostProductSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsProductOwner]

    queryset = Product.objects.all()
    serializer_class = PostProductSerializer
