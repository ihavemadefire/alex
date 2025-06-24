from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomUserUpdateForm,
)
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("users:login")


class SignInView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "login.html"


class SignOutView(LogoutView):
    next_page = reverse_lazy("home")


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = "profile.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self):
        return self.request.user  # Only allow editing the current user
