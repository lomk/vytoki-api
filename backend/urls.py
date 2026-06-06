from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
import django.conf.urls.i18n as i18n_urls

urlpatterns = [
    path("i18n/", include(i18n_urls)),
    path("api/", include("api.urls")),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    prefix_default_language=False,
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

