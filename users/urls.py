from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name='registration_view'),
    path("login/", views.NewLoginView.as_view(), name='login_view'),
    path("users/", views.UserListView.as_view(), name='user_listview'),
]