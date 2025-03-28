from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from config import settings
from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierViewSet

app_name = SuppliersConfig.name

router = DefaultRouter()
router.register("", SupplierViewSet, basename="suppliers")

urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)