from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from companies.filters import CompanyFilter
from companies.models import Company
from companies.permissions import IsActive
from companies.serializer import CompanySerializer


class CompanyViewSet(ModelViewSet):
    """ViewSet для модели COMPANY"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CompanyFilter
    ordering_fields = '__all__'
