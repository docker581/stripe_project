from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

handler404 = "payments.views.page_not_found"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
