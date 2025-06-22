from django.urls import path
from .views import SignUpView, SignInView, SignOutView, UserProfileUpdateView

app_name = "users"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", SignInView.as_view(), name="login"),
    path("logout/", SignOutView.as_view(), name="logout"),
    path("profile/", UserProfileUpdateView.as_view(), name="profile"),
]
