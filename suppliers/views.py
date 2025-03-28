from rest_framework.viewsets import ModelViewSet

from suppliers.models import Supplier
from suppliers.serializer import SupplierSerializer


class SupplierViewSet(ModelViewSet):
    """ViewSet для модели SUPPLIER"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
