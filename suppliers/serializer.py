from rest_framework import serializers

from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели SUPPLIER """

    class Meta:
        model = Supplier
        fields = '__all__'
