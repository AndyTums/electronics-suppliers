from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Функциональность админ панели для модели PRODUCTS """

    list_display = ('id', 'title', 'model', 'release_date', 'created_at', 'updated_at')
