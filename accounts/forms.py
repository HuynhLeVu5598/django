from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)


# UserCreationForm tạo một biểu mẫu đăng ký người dùng mới


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


# UserChangeForm cập nhật các form để cập nhật người dùng hiện tại,
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


from allauth.account.forms import ResetPasswordForm


class CustomPasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control"})
