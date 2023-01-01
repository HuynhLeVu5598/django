from django.contrib import admin
from .models import Book, Review

# admin.site.register(Book)

# TabularInline tất cả các trường mô hình xuất hiện trên một dòng
# StackedInline mỗi trường có một dòng riêng
class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    # thêm ReviewInline vào trang quản lý
    inlines = [
        ReviewInline,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )


admin.site.register(Book, BookAdmin)
