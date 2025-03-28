from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("users.urls", namespace="users")),
    path("supplier/", include("suppliers.urls", namespace="supplier")),
    path("product/", include("suppliers.urls", namespace="products"))
]

# path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
# path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
