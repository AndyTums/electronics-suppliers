from django.db import models
from django.core.exceptions import ValidationError


class Company(models.Model):
    """Модель: Компании"""

    CATEGORY_CHOICE = [

        ('factory', 'Производство с завода'),
        ('retail', 'Розничная продажа'),
        ('individual entrepreneur', 'Индивидуальный предприниматель')
    ]

    title = models.CharField(
        max_length=150, verbose_name="Название компании"
    )
    category = models.CharField(
        choices=CATEGORY_CHOICE, verbose_name="Вид деятельности"
    )
    email = models.EmailField(
        unique=True, verbose_name="Почта"
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна"
    )
    city = models.CharField(
        max_length=50, verbose_name="Город"
    )
    street = models.CharField(
        max_length=50, verbose_name="Улица"
    )
    house_number = models.CharField(
        max_length=10, verbose_name="Номер дома"
    )
    supplier = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Поставщик", blank=True, null=True)
    duty_supplier = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность перед поставщиком"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"Название: {self.title}, Вид деятельности: {self.category}"

    def clean(self):
        """ Валидация полей """

        # Проверка, что комания не может быть поставщиком самой у себя
        if self == self.supplier:
            raise ValidationError(
                "Компания не может быть поставщиком самой у себя.")

        # Проверка, что завод может ссылаться только на другой завод как на поставщика
        if self.category == 'factory' and self.supplier:
            if self.supplier.category == 'individual entrepreneur' or self.supplier.category == 'retail':
                raise ValidationError(
                    "Завод не может выбирать поставщика, у которого вид деятельности: ИП или Розничная торговля.")

        # Проверка, что розн.торговля может ссылаться только на завод как на поставщика
        if self.category == 'retail' and self.supplier:
            if self.supplier.category == 'individual entrepreneur' or self.supplier.category == 'retail':
                raise ValidationError(
                    "Розничная торговля может закупать товар только у завода.")

        # Проверка, что ИП может ссылаться только на завод/розн.торговлю как на поставщика
        if self.category == 'individual entrepreneur' and self.supplier:
            if self.supplier.category == 'individual entrepreneur':
                raise ValidationError(
                    "ИП может закупать товары только у розничных продавцов или завода.")

    def save(self, *args, **kwargs):
        """ Сохраняем изменения после валидаций """

        self.clean()
        super().save(*args, **kwargs)
