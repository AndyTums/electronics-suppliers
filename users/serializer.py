from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели USER """

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'country', 'photo']
