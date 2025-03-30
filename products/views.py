from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from products.filters import ProductFilter
from products.models import Product
from products.serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    """ViewSet для модели PRODUCT"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = '__all__'
