from django.urls import path, re_path
from . import views
from django.urls import include
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]