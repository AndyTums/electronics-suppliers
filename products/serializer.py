from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели PRODUCT """

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Product
        fields = ['title', 'model', 'release_date', 'created_at', 'implementer']
