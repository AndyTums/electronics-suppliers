from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.filters import UserFilter
from users.models import User

from users.serializer import UserSerializer


class UserViewSet(ModelViewSet):
    """ViewSet для модели USER"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = UserFilter
    ordering_fields = '__all__'
