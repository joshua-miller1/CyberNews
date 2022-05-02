from django.urls import path
from . import views
#from .views import SignUpView
from .views import SignUpForm

# URL Configuration module - URL configuation
urlpatterns = [
    path('', views.say_hello),
    path('signup/', views.signup_view),
    #path('signup/', SignUpView.as_view(), name="signup"),
]