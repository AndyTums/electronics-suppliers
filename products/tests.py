from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status

from products.models import Product
from users.models import User
from .models import Company


class ProductTest(APITestCase):
    """ Тест модели PRODUCT """

    def setUp(self):
        """ Прописывем исходные данные и необходимые параметры """

        # Очищаем всю БД для корректной работы
        Company.objects.all().delete()
        Product.objects.all().delete()
        User.objects.all().delete()

        # Создаем активного пользователя
        self.user = User.objects.create(email='forTEST@mail.ru', is_active=True)

        # Создаем модель компании
        self.company = Company.objects.create(title='Test', category='factory', email='test@mail.ru', country='Россия',
                                              city='Севас', street='Ленина', house_number='1')

        # Создаем модель продукта
        self.product = Product.objects.create(title='TestProduct', model='testmodul', release_date="2025-04-02")

        # Авторизируемся под нашим пользователем
        self.client.force_authenticate(user=self.user)

    def test_product_create(self):
        """ Тестирование создание обьекта PRODUCT """

        # Задаем параметры обькта для создания
        data = {
            'title': 'TESTproductcreate',
            'model': 'testmodulcreate',
            'release_date': "2024-04-02"
        }

        # Делаем запрос к API для создания объекта
        response = self.client.post(
            '/product/',
            data=data
        )

        # Сверяем статус код
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Сверяем ожидаемое количество PRODUCT в БД
        self.assertEqual(
            Product.objects.count(),
            2
        )

        # Преобразуем время создания/обновления в локальное время
        created_at_local = timezone.localtime(self.product.created_at)
        updated_at_local = timezone.localtime(self.product.updated_at)

        # Форматируем время в необходимый нам шаблон
        created_product_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
        created_product_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            response.json(),
            {'title': 'TESTproductcreate', 'model': 'testmodulcreate', 'release_date': '2024-04-02',
             'created_at': created_product_created_at, 'updated_at': created_product_updated_at,
             'implementer': []}
        )

    def test_product_list(self):
        """ Тест списка всех PRODUCT в БД """

        # Создаем ссылку для нашего запроса
        url = reverse('products:products-list')

        # Делаем запрос передавая нашу ссылку
        response = self.client.get(url)

        # Формируем полученный ответ в формате JSON
        data = response.json()

        # Сверяем статус кода
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Преобразуем время создания/обновления в локальное время
        created_at_local = timezone.localtime(self.product.created_at)
        updated_at_local = timezone.localtime(self.product.updated_at)

        # Форматируем время в необходимый нам шаблон
        created_product_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
        created_product_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            data,
            [{'title': 'TestProduct', 'model': 'testmodul', 'release_date': '2025-04-02',
              'created_at': created_product_created_at, 'updated_at': created_product_updated_at, 'implementer': []}]

        )

        # Сверяем ожидаемое количество PRODUCT в БД
        self.assertEqual(
            Product.objects.count(),
            1
        )

    def test_product_retrieve(self):
        """ Тест детальной информации обьекта PRODUCT """

        # Создаем ссылку для нашего запроса
        url = reverse('products:products-detail', args=(self.product.pk,))

        # Делаем запрос передавая нашу ссылку
        response = self.client.get(url)

        # Формируем полученный ответ в формате JSON
        data = response.json()

        # Сверяем статус кода
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Преобразуем время создания/обновления в локальное время
        created_at_local = timezone.localtime(self.product.created_at)
        updated_at_local = timezone.localtime(self.product.updated_at)

        # Форматируем время в необходимый нам шаблон
        created_product_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
        created_product_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            data,
            {'title': 'TestProduct', 'model': 'testmodul', 'release_date': '2025-04-02',
             'created_at': created_product_created_at, 'updated_at': created_product_updated_at, 'implementer': []}

        )

    def test_product_update(self):
        """ Тестирование обновление объекта PRODUCT """

        # Создаем ссылку для нашего запроса
        url = reverse('products:products-detail', args=(self.product.pk,))

        # Формируем данные для изменения
        data = {
            'title': 'TestProductupdate',
            'model': 'testmodulupdate',
            'implementer': [self.company.pk]
        }

        # Делаем запрос передавая нашу ссылку
        response = self.client.patch(url, data=data)

        # Сверяем статус код
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Сверяем ожидаемое количество PRODUCT в БД
        self.assertEqual(
            Product.objects.count(),
            1
        )

        # Преобразуем время создания/обновления в локальное время
        created_at_local = timezone.localtime(self.product.created_at)
        updated_at_local = timezone.localtime(self.product.updated_at)

        # Форматируем время в необходимый нам шаблон
        created_product_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
        created_product_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            response.json(),
            {'title': 'TestProductupdate', 'model': 'testmodulupdate', 'release_date': '2025-04-02',
             'created_at': created_product_created_at, 'updated_at': created_product_updated_at,
             'implementer': ['Test']}

        )

    def test_product_delete(self):
        """ Тестирование удаление обьекта PRODUCT """

        # Создаем ссылку для нашего запроса
        url = reverse('products:products-detail', args=(self.product.pk,))

        # Делаем запрос передавая нашу ссылку
        response = self.client.delete(url)

        # Сверяем статус код
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Сверяем ожидаемое количество PRODUCT в БД
        self.assertEqual(
            Product.objects.count(),
            0
        )
