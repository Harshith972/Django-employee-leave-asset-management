from django.urls import path
from .views import register, login_view, home, logout_view, change_password,profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("home/", home, name="home"),
    path("logout/", logout_view, name="logout"),
    path("change-password/", change_password, name="change_password"),
    path("profile/", profile, name="profile"),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/change_password.html"
        ),
        name="change_password",
    ),
]