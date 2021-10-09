from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from .views import hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello.as_view(), name='hello'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
