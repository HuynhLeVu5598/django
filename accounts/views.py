from django.shortcuts import render, reverse
from .forms import (
    CustomPasswordResetForm,
    CustomPasswordChangeForm,
    CustomResetPasswordKeyForm,
)

# Create your views here.
from allauth.account.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordSetView,
    PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView,
)

from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "account/password_reset_done.html"


class CustomPasswordResetView(PasswordResetView):
    template_name = "account/password_reset_form.html"
    form_class = CustomPasswordResetForm


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "account/change_password.html"
    form_class = CustomPasswordChangeForm

    def form_valid(self, form):
        # Sử dụng form.save() để cập nhật mật khẩu mới
        form.save()
        # Gọi phương thức form_valid của lớp SetPasswordView cha
        # response = super().form_valid(form)
        # Trả về một đối tượng HttpResponse với template tùy chỉnh có chứa thông báo thành công
        return render(
            self.request,
            "account/change_password_successed.html",
            {"success_message": "Your new password has been changed successfully!"},
        )


# class CustomSetPasswordView(PasswordSetView):
#     def form_valid(self, form):
#         # Sử dụng form.save() để cập nhật mật khẩu mới
#         form.save()
#         messages.success(
#             self.request, "Mật khẩu mới của bạn đã được cập nhật thành công!"
#         )
#         return super().form_valid(form)

#     # Xác định template tùy chỉnh cho trang này
#     template_name = "account/custom_set_password.html"


class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    def form_valid(self, form):
        # Gọi phương thức form_valid của lớp cha
        # response = super().form_valid(form)
        # Sử dụng form.save() để cập nhật mật khẩu mới
        form.save()
        # Thay đổi thông báo thành công
        messages.success(self.request, "Mật khẩu mới của bạn đã được đặt thành công!")
        # Điều hướng người dùng đến trang mà bạn muốn họ đến sau khi đặt lại mật khẩu thành công
        return redirect(reverse("custom_reset_password_key_done"))

    template_name = "account/custom_reset_password_from_key.html"
    # form_class = CustomResetPasswordKeyForm

    # success_url = reverse_lazy("account_reset_password_from_key_done")


class CustomPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    template_name = "account/password_reset_from_key_done.html"
