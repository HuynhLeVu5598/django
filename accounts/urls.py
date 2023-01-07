from django.urls import path, include, re_path
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordChangeView,
    # CustomSetPasswordView,
    CustomPasswordResetFromKeyView,
    CustomPasswordResetFromKeyDoneView,
)

urlpatterns = [
    # trang nhập email để reset password
    # Sử dụng path để khai báo một URL pattern có dạng cố định
    path(
        "password/reset/",
        CustomPasswordResetView.as_view(),
        name="account_reset_password",
    ),
    # trang hiển thị đã gửi email rest password thành công
    path(
        "password/reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    # trang thay đổi mật khẩu khi đã đăng nhập thành công
    path(
        "password/change/", CustomPasswordChangeView.as_view(), name="change_password"
    ),
    # trang thay đổi mật khẩu khi quên mật khẩu, lấy url từ email
    # Re-path là một thư viện bên ngoài Django dùng để tạo và khớp các URL patterns.
    # Sử dụng re-path để khai báo một URL pattern có dạng động
    # sử dụng regular expressions để khớp với các URL có dạng khác nhau
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        CustomPasswordResetFromKeyView.as_view(),
        name="account_reset_password_from_key",
    ),
    # trang hiển thị đã thay đổi mật khẩu (khi quên mật khẩu) thành công
    path(
        "password/reset/key/done/",
        CustomPasswordResetFromKeyDoneView.as_view(),
        name="custom_reset_password_key_done",
    ),
    path("", include("allauth.urls")),
    # /github/login/?next=/accounts/login/
]
