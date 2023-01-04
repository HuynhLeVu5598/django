from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from .models import Todo
from .serializers import BookSerializer, TodoSerializer

# ListAPIView dùng để hiển thị danh sách các object


class BookAPIView(generics.ListAPIView):
    # Phương thức get_queryset trả về danh sách các object cần hiển thị
    queryset = Book.objects.all()
    # phương thức serializer_class trả về serializer sử dụng để chuyển đổi danh sách object thành dữ liệu json
    serializer_class = BookSerializer

# hiển thị tất cả todo


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# hiển thị một thể hiện mô hình duy nhất


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
