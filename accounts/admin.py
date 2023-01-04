from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
        "is_superuser",
    ]


#  các trường sử dụng trong một bố cục để hiển thị trên trang quản lý người dùng
# hiển thị trên trang quản lý người dùng và trong hộp thoại tạo người dùng mới
fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
