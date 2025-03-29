from rest_framework.viewsets import ModelViewSet

from companies.models import Company
from companies.serializer import CompanySerializer


class CompanyViewSet(ModelViewSet):
    """ViewSet для модели SUPPLIER"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
