from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    """ViewSet для модели PRODUCT"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
