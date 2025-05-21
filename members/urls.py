#from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
#from django.conf.urls.static import static

from . import views
app_name = 'members'
urlpatterns = [
    path("", views.homepage, name="home"),
    path("members/", views.members_list, name='members'),
    path("add_member/", views.add_member, name='add_member'),
    path('login/', auth_views.LoginView.as_view(template_name='home.html', authentication_form=LoginForm), name='login')
]

"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
"""
