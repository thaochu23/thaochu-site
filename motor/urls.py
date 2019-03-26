from django.urls import path
from . import views

urlpatterns = [
    path('', views.motor_motor),
    path('<int:id>', views.controlDevice, name='controlDevice'),
]