from django.contrib import admin, messages

from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Функциональность админ панели для модели COMPANY """

    list_display = ('id', 'title', 'category', 'email', 'country', 'city', 'admin_link', 'duty_supplier')
    readonly_fields = ('admin_link', 'id')
    list_filter = ('category', 'country', 'city')
    search_fields = ('title', 'email', 'country', 'city', 'street')
    actions = ['clear_debt', ]

    def clear_debt(self, request, queryset):
        """ Функция обнуления задолжности перед поставщиком """

        updated = queryset.update(duty_supplier=0.00)
        self.message_user(
            request,
            f"Задолженность очищена у {updated} компаний",
            messages.SUCCESS
        )

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
