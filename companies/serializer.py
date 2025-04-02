from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели COMPANY """

    # Делаем удобный формат времени
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Company
        fields = ('title', 'category', 'email', 'country', 'city', 'street', 'house_number', 'supplier',
                  'products', 'link', 'duty_supplier', 'created_at', 'updated_at', 'link')
        read_only_fields = ['duty_supplier', 'created_at', 'updated_at']

    def to_representation(self, instance):
        """ Преобразования формата вывода API запроса """

        # Получаем стандартное представление
        representation = super().to_representation(instance)

        # Получаем список продуктов
        products_list = instance.products.all()

        # Получаем название компании по ее ID
        if representation['supplier'] is not None:
            supplier_title = Company.objects.get(id=representation['supplier']).title
        else:
            supplier_title = "Поставщик отсутствует"

        # Форматируем необходимый шаблон вывода API
        formatted_output = {

            # Название компании
            "title": representation['title'],
            # Вид деятельности компании
            "category": representation['category'],

            # Контакты компании
            "contacts": {
                "email": representation['email'],
                "country": representation['country'],
                "city": representation['city'],
                "street": representation['street'],
                "house_number": representation['house_number'],
            },

            # Получаем подробную информацию о компании
            "supplier": supplier_title,
            "duty_supplier": representation['duty_supplier'],
            "supplier_link": representation['link'],
            "created_at": representation['created_at'],

            # Список названий продуктов (с помощью генератора)
            "products": [
                {
                    "title": product.title,
                    "model": product.model,
                    "release_date": product.release_date,
                }
                for product in products_list
            ] if products_list else ["Нет продуктов в реализации"]

        }

        return formatted_output
