from django.urls import path
from . import views

# URL Configuration module - URL configuation
urlpatterns = [
    path('', views.get_cyber_news_links)
]