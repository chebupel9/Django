from django.urls import path, re_path
from . import views
from django.urls import include
from django.contrib import admin

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('', include('main.urls'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail')
]