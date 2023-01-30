from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.DynamoRequest.as_view(), name='create_device'),
    path('devices/id<pk>/', views.DynamoDetailRequest.as_view(), name='get_device'),
]