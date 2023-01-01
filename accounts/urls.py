from django.urls import path, include
from .views import CustomPasswordResetView

urlpatterns = [
    path(
        "password/reset/",
        CustomPasswordResetView.as_view(),
        name="account_reset_password",
    ),
    path("", include("allauth.urls")),
]
