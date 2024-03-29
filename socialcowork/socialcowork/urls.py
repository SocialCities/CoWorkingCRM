from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crm/', include('crm.urls')), #Include from app crm
    url(r'^', include('main.urls')), #Include from app main
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
