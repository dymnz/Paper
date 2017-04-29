from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^system/', include('system.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
]