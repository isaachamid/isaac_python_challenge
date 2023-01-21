from django.urls import path
from . import views


urlpatterns = [
    path('devices', views.create_device, name='create_device'),
    path('devices/<int:pk>/', views.get_device, name='get_device'),
]