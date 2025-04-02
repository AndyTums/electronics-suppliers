from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели USER """

    # Делаем удобный формат времени
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'country', 'photo', 'created_at', 'updated_at']
