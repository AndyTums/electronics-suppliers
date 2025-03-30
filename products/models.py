from django.db import models

from companies.models import Company


class Product(models.Model):
    """Модель: ТОВАР"""

    title = models.CharField(
        max_length=150, verbose_name="Название товара"
    )
    model = models.CharField(
        max_length=150, verbose_name="Модель товара"
    )
    release_date = models.DateField(
        verbose_name="Дата выпуска"
    )
    implementer = models.ManyToManyField(
        Company, verbose_name="Реализатор", related_name="products"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title
