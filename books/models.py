from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

# Create your models here.
# books/models.py
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,  #  dùng uuid4 cho việc mã hóa.
        editable=False,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # null = True: đánh dấu một giá trị trống trong cơ sở dữ liệu
    # blank = True: mô hình được phép có giá trị trống
    cover = models.ImageField(upload_to="covers/", blank=True)  # MEDIA_ROOT/covers
    # "Meta" là một lớp trong Django cho phép bạn định nghĩa các thuộc tính mà không phải là trường dữ liệu của mô hình
    # tác giả có thể đọc tất cả sách. nói cách khác họ có quyền truy cập vào DetailView
    class Meta:
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    # đặt một url chuẩn cho mô hình
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class Review(models.Model):  # new
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",  # để làm cho việc theo dõi khóa ngoại dễ dàng hơn
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),  # để tham khảo mô hình người dùng tùy chỉnh
        # on_delete xác định hành động sẽ được thực hiện khi một bản ghi liên kết tới bảng khác bị xóa
        # CASCADE xóa tất cả các bản ghi liên kết tới bảng khác khi bản ghi đó bị xóa
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
