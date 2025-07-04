from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("media/", include("media.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("auth/", include("django.contrib.auth.urls")),
]
