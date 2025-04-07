import django_filters

from products.models import Product


class ProductFilter(django_filters.FilterSet):
    """Фильтры для модели PRODUCT """

    class Meta:
        model = Product
        fields = ['title', 'model', 'release_date', 'created_at']
