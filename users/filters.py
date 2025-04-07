import django_filters

from users.models import User


class UserFilter(django_filters.FilterSet):
    """Фильтры для модели USER """

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'country']
