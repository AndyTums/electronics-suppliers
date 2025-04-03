from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status

from products.models import Product
from users.models import User
from .models import Company


class CompanyTest(APITestCase):
    """ Тест модели COMPANY """

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

        # Авторизируемся под нашим пользователем
        self.client.force_authenticate(user=self.user)

    def test_company_create(self):
        """ Тестирование создание обьекта COMPANY """

        # Задаем параметры обькта для создания
        data = {
            'title': 'TESTcreate123',
            'category': 'factory',
            'email': 'TEST@gmail.com',
            'country': 'Testcountr',
            'city': 'TESTcity',
            'street': 'TESstreet',
            'house_number': '1',
        }

        # Делаем запрос к API для создания объекта
        response = self.client.post(
            '/company/',
            data=data
        )

        # Сверяем статус код
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Сверяем ожидаемое количество COMPANY в БД
        self.assertEqual(
            Company.objects.count(),
            2
        )

        # Получаем объект компании
        company = Company.objects.get(title="TESTcreate123")

        # Преобразуем время создания в локальное время
        created_at_local = timezone.localtime(company.created_at)

        # Форматируем время в необходимый нам шаблон
        created_company_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            response.json(),
            {'title': 'TESTcreate123', 'category': 'factory',
             'contacts': {
                 'email': 'TEST@gmail.com', 'country': 'Testcountr',
                 'city': 'TESTcity', 'street': 'TESstreet',
                 'house_number': '1'
             },
             'supplier': 'Поставщик отсутствует', 'duty_supplier': '0.00',
             'supplier_link': None, 'created_at': created_company_created_at,
             'products': ['Нет продуктов в реализации']}
        )

    def test_company_list(self):
        """ Тест списка всех COMPANY в БД """

        # Создаем ссылку для нашего запроса
        url = reverse('companies:companies-list')

        # Делаем запрос передавая нашу ссылку
        response = self.client.get(url)

        # Формируем полученный ответ в формате JSON
        data = response.json()

        # Сверяем статус кода
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Преобразуем время создания в локальное время
        created_at_local = timezone.localtime(self.company.created_at)

        # Форматируем время в необходимый нам шаблон
        created_company_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            data,
            [
                {'title': 'Test', 'category': 'factory',
                 'contacts': {
                     'email': 'test@mail.ru', 'country': 'Россия', 'city': 'Севас', 'street': 'Ленина',
                     'house_number': '1'
                 },
                 'supplier': 'Поставщик отсутствует', 'duty_supplier': '0.00',
                 'supplier_link': None, 'created_at': created_company_created_at,
                 'products': [
                     'Нет продуктов в реализации']
                 }
            ]

        )

        # Сверяем ожидаемое количество COMPANY в БД
        self.assertEqual(
            Company.objects.count(),
            1
        )

    def test_company_retrieve(self):
        """ Тест детальной информации обьекта COMPANY """

        # Создаем ссылку для нашего запроса
        url = reverse('companies:companies-detail', args=(self.company.pk,))

        # Делаем запрос передавая нашу ссылку
        response = self.client.get(url)

        # Формируем полученный ответ в формате JSON
        data = response.json()

        # Сверяем статус кода
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Преобразуем время создания в локальное время
        created_at_local = timezone.localtime(self.company.created_at)

        # Форматируем время в необходимый нам шаблон
        created_company_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            data,
            {'title': 'Test', 'category': 'factory',
             'contacts': {
                 'email': 'test@mail.ru', 'country': 'Россия', 'city': 'Севас', 'street': 'Ленина',
                 'house_number': '1'},
             'supplier': 'Поставщик отсутствует', 'duty_supplier': '0.00',
             'supplier_link': None, 'created_at': created_company_created_at,
             'products': ['Нет продуктов в реализации']
             }

        )

    def test_company_update(self):
        """ Тестирование обновление обьекта COMPANY """

        # Создаем ссылку для нашего запроса
        url = reverse("companies:companies-detail", args=(self.company.pk,))

        # Формируем данные для изменения
        data = {
            'title': 'TestUPDATE',
            'city': 'Севас',
            'duty_supplier': '0.00'  # Данный параметр останется преждним, т.к отключено его изменения через API
        }

        # Делаем запрос передавая нашу ссылку
        response = self.client.patch(url, data=data)

        # Сверяем статус код
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Сверяем ожидаемое количество COMPANY в БД
        self.assertEqual(
            Company.objects.count(),
            1
        )

        # Преобразуем время создания в локальное время
        created_at_local = timezone.localtime(self.company.created_at)

        # Форматируем время в необходимый нам шаблон
        created_company_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')

        # Сверяем данные с ожидаемыми
        self.assertEqual(
            response.json(),
            {'title': 'TestUPDATE', 'category': 'factory',
             'contacts': {
                 'email': 'test@mail.ru', 'country': 'Россия', 'city': 'Севас', 'street': 'Ленина',
                 'house_number': '1'},
             'supplier': 'Поставщик отсутствует', 'duty_supplier': '0.00',
             'supplier_link': None, 'created_at': created_company_created_at,
             'products': ['Нет продуктов в реализации']}

        )

    def test_company_delete(self):
        """ Тестирование удаление обьекта COMPANY """

        # Создаем ссылку для нашего запроса
        url = reverse("companies:companies-detail", args=(self.company.pk,))

        # Делаем запрос передавая нашу ссылку
        response = self.client.delete(url)

        # Сверяем статус код
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Сверяем ожидаемое количество COMPANY в БД
        self.assertEqual(
            Company.objects.count(),
            0
        )
