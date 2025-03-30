import django_filters

from companies.models import Company


class CompanyFilter(django_filters.FilterSet):
    """Фильтры для модели COMPANY """

    class Meta:
        model = Company
        fields = ['country', 'city', 'street', 'title', 'category',]
