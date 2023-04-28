from django.urls import path, re_path
from . import views
from django.urls import include
from django.contrib import admin

urlpatterns = [
    path('', views.order_home, name='order_home'),
    path('', include('main.urls'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('create', views.order_create, name='create'),
    path('<int:pk>', views.OrderDetailView.as_view(), name='order_detail')
]