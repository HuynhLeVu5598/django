# get_user_model là một hàm trong Django cung cấp cho phép bạn lấy ra model User hiện tại đang được sử dụng trong dự án của bạn
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from allauth.account.forms import (
    ResetPasswordForm,
    ChangePasswordForm,
    SetPasswordForm,
    ResetPasswordKeyForm,
)
from django import forms

# UserCreationForm tạo một biểu mẫu đăng ký người dùng mới
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", "name")


# UserChangeForm cập nhật các form để cập nhật người dùng hiện tại,
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", "name")


# ResetPasswordForm là một form có sẵn trong Django để xử lý quá trình reset password của người dùng. Form này bao gồm các trường sau:
# email: trường nhập email của người dùng, được sử dụng để gửi email reset password tới người dùng.
class CustomPasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        # 3 cách kế thừa từ lớp cha:
        super().__init__(*args, **kwargs)  # cách 1
        # ResetPasswordForm.__init__(self, *args, **kwargs)  # cách 2
        # super(CustomPasswordResetForm, self).__init__(*args, **kwargs) # cách 3
        # Đoạn code dưới sử dụng thuộc tính attrs của đối tượng widget để thêm thuộc tính class vào thẻ HTML input đại diện cho trường email
        # Widget là một tính năng của Django form field cho phép bạn điều chỉnh cách mà một trường form được hiển thị trên trang web
        # "form-control" là một class được sử dụng trong Bootstrap để tạo ra một form field giao diện người dùng. nó sẽ tạo ra một bề mặt trơn trên cho form field và có thể thêm một viền tròn cho nút submit
        self.fields["email"].widget.attrs.update({"class": "form-control"})


class CustomPasswordChangeForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        # Thay đổi cách hiển thị trường mật khẩu
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"placeholder": "New password"}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"placeholder": "Confirm new password"}
        )

        # Thay đổi label của các trường mật khẩu
        self.fields["oldpassword"].label = "Old Password"
        self.fields["password1"].label = "New Password"
        self.fields["password2"].label = "Confirm New Password"


# class CustomSetPasswordForm(SetPasswordForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Thêm trường mới vào form
#         self.fields["phone_number"] = forms.CharField()
#         # Thay đổi cách hiển thị trường mật khẩu
#         self.fields["password1"].widget = forms.PasswordInput(
#             attrs={"placeholder": "New password"}
#         )
#         self.fields["password2"].widget = forms.PasswordInput(
#             attrs={"placeholder": "Confirm new password"}
#         )


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):

    # Tạo các trường dữ liệu mật khẩu mới và xác nhận mật khẩu mới
    # new_password1 = forms.CharField(label="Mật khẩu mới", widget=forms.PasswordInput)
    # new_password2 = forms.CharField(
    #     label="Xác nhận mật khẩu mới", widget=forms.PasswordInput
    # )

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError("Mật khẩu phải dài hơn 8 ký tự.")
        return password1

    # def clean(self):
    #     # Lấy giá trị của các trường dữ liệu mật khẩu mới và xác nhận mật khẩu mới
    #     new_password1 = self.cleaned_data.get('new_password1')
    #     new_password2 = self.cleaned_data.get('new_password2')

    #     # Kiểm tra xem các trường dữ liệu mật khẩu mới và xác nhận mật khẩu mới có khớp nhau hay không
    #     if new_password1 and new_password2 and new_password1 != new_password2:
    #         raise forms.ValidationError("Mật khẩu mới và xác nhận mật khẩu mới không khớp nhau.")
    #     return self.cleaned_data
