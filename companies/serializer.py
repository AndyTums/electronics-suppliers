from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели COMPANY """

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Company
        fields = ('title', 'category', 'email', 'country', 'city', 'street', 'house_number', 'supplier',
                  'duty_supplier', 'products', 'link', 'created_at')
