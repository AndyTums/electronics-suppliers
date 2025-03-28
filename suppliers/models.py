from django.db import models
from django.core.exceptions import ValidationError


class Supplier(models.Model):
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
    related_supplier = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Поставщик", blank=True, null=True)
    duty_supplier = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
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

        # Проверка, что завод не может ссылаться на ИП и на розничную продажу
        if (self.category == 'factory' and self.supplier
                and self.related_supplier.category == 'individual entrepreneur'
                or self.related_supplier.category == 'retail'):
            raise ValidationError(
                "Завод не может выбирать поставщика, у которого вид деятельности: ИП или Розничная торговля.")

    def save(self, *args, **kwargs):
        """ Сохраняем изменения после валидаций """

        self.clean()
        super().save(*args, **kwargs)
