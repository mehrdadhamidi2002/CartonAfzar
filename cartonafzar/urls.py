from django.contrib import admin
from django.urls import path, include
from tss.views import home
from django.conf import settings
from django.conf.urls.static import static

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tss.urls'), name='home'),
    path('django-check-seo/', include('django_check_seo.urls')),
    path('sentry-debug/', trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)