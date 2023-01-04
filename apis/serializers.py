# Một serializer dịch dữ liệu phức tạp như bộ truy vấn và phiên bản mô hình sang định dạng dễ sử dụng điển hình là JSON
from rest_framework import serializers
from books.models import Book
from .models import Todo


class BookSerializer(serializers.ModelSerializer):
    #  Meta được sử dụng để định nghĩa các thuộc tính đặc biệt cho các lớp
    class Meta:
        model = Book
        # các trường hiển thị
        fields = ("title", "author", "price")


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
        )
