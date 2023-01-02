from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

# ListAPIView dùng để hiển thị danh sách các object
class BookAPIView(generics.ListAPIView):
    # Phương thức get_queryset trả về danh sách các object cần hiển thị
    queryset = Book.objects.all()
    # phương thức serializer_class trả về serializer sử dụng để chuyển đổi danh sách object thành dữ liệu json
    serializer_class = BookSerializer