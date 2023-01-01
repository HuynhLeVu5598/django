from django.shortcuts import render
from .forms import CustomPasswordResetForm

# Create your views here.
from allauth.account.views import PasswordResetView, PasswordResetDoneView


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset_form.html"
    form_class = CustomPasswordResetForm
