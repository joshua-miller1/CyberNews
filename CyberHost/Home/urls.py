from django.urls import path
from . import views

# URL Configuration module - URL configuation
urlpatterns = [
    path('Home/', views.say_hello)
]