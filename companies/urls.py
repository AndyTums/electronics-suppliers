from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from config import settings
from companies.apps import CompaniesConfig
from companies.views import CompanyViewSet

app_name = CompaniesConfig.name

router = DefaultRouter()
router.register("", CompanyViewSet, basename="companies")

urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
