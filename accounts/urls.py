from django.urls import path, include
from .views import CustomPasswordResetView, CustomPasswordResetDoneView

urlpatterns = [
    path(
        "password/reset/",
        CustomPasswordResetView.as_view(),
        name="account_reset_password",
    ),
    path(
        "password/reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path("", include("allauth.urls")),
]
