from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm



app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(
        template_name="blog/login.html",
        authentication_form=LoginForm), name="login"),
]
