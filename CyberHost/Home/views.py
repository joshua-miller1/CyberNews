from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

# Create your views here.


def say_hello(request):
    return render(request, 'Home.html')
    # return HttpResponse('Hello!')


def signup_view(request1):
    context1 = {}
    context1['form'] = SignUpForm()
    success_url = reverse_lazy('login')
    return render(request1, "registration/signup.html", context1)


#class SignUpView(generic.CreateView):
#    #   form_class = UserCreationForm()
#    form_class = SignUpForm()
#    success_url = reverse_lazy("login")
#  template_name = "registration/signup.html"
