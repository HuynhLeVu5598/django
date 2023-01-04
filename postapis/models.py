from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # auto_now_add tự động cập nhật giá trị của một trường khi tạo một bản ghi mới
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now cập nhật giá trị của trường khi bản ghi được lưu lại
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
