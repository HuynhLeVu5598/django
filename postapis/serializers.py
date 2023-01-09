from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model  # new

# Viewsets cung cấp một cách dễ dàng để xác định các hành động CRUD (create, retrieve, update, delete)
# trên một tập hợp các đối tượng được lưu trữ trong cơ sở dữ liệu.
from rest_framework import viewsets
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly  # new


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        model = Post


class UserSerializer(serializers.ModelSerializer):  # new
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )


class PostViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
