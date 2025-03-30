from django.contrib import admin, messages

from companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Функциональность админ панели для модели COMPANY """

    list_display = ('title', 'category', 'email', 'country', 'admin_link', 'duty_supplier')
    readonly_fields = ('admin_link',)
    list_filter = ('category', 'country')
    search_fields = ('title', 'email')
    actions = ['clear_debt', ]

    def clear_debt(self, request, queryset):
        updated = queryset.update(duty_supplier=0.00)
        self.message_user(
            request,
            f"Задолженность очищена у {updated} компаний",
            messages.SUCCESS
        )

    clear_debt.short_description = "Очистить задолженность перед поставщиком"
