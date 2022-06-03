from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, LoginForm


class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = "registration.html"
    success_url = "/login/"


class NewLoginView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = "/books/"

    def get_success_url(self):
        return self.success_url


class UserListView(generic.ListView):
    template_name = "users.html"
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset