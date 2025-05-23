from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings 
from django.urls import path, include,re_path
from django.conf.urls.static import static
urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('members.urls')),
]
