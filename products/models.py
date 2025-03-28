from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    """Модель: Компании"""

    title = models.CharField(
        max_length=150, verbose_name="Название продукта"
    )
    model = models.CharField(
        max_length=150, verbose_name="Модель продукта"
    )
    release_date = models.DateField(
        verbose_name="Дата выпуска"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
