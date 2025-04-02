from rest_framework import serializers

from companies.models import Company
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели PRODUCT """

    # Делаем удобный формат времени
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Product
        fields = ['title', 'model', 'release_date', 'created_at', 'updated_at', 'implementer']

    def to_representation(self, instance):
        """ Преобразования формата вывода API запроса """

        # Получаем стандартное представление
        representation = super().to_representation(instance)

        # Список для названий компаний
        implementer_titles = []

        # Получаем название компаний и добовляем их в список
        if representation['implementer']:
            for imp in representation['implementer']:
                implementers = Company.objects.get(id=imp).title
                implementer_titles.append(implementers)
        else:
            implementers = "Поставщик отсутствует"

        # Форматируем необходимый шаблон вывода API
        formatted_output = {

            # Название продукта
            "title": representation['title'],

            # Модель продукта
            "model": representation['model'],

            # Дата релиза
            "release_date": representation['release_date'],

            # Дата добавления продукта в БД
            "created_at": representation['created_at'],

            # Реализаторы продукта
            "implementer": implementer_titles,


        }

        return formatted_output
