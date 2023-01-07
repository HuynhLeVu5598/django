from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly  # new
from rest_framework.permissions import IsAdminUser  # new


# ListCreateAPIView tạo và trả về danh sách các đối tượng
class PostListAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# RetrieveUpdateDestroyAPIView cho phép người dùng lấy, cập nhật và xóa một đối tượng cụ thể từ cơ sở dữ liệu
class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # chỉ quản trị viên mới có thể xem trang chi tiết
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
