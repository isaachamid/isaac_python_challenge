from django.urls import path
from . import views


urlpatterns = [
    path('devices', views.CreateDeviceAPIView.as_view(), name='create_device'),
    path('devices/<pk>/', views.GetDeviceAPIView.as_view(), name='get_device'),
]