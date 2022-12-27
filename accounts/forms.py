from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
# from allauth.account.forms import PasswordResetForm


class CustomPasswordResetForm(PasswordResetForm):
    pass

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
