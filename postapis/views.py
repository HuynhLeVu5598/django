from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

# ListCreateAPIView tạo và trả về danh sách các đối tượng


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# RetrieveUpdateDestroyAPIView cho phép người dùng lấy, cập nhật và xóa một đối tượng cụ thể từ cơ sở dữ liệu


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # chỉ quản trị viên mới có thể xem trang chi tiết
    permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
