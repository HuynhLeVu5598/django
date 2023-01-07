from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model  # new

# Viewsets cung cấp một cách dễ dàng để xác định các hành động CRUD (create, retrieve, update, delete)
# trên một tập hợp các đối tượng được lưu trữ trong cơ sở dữ liệu.
from rest_framework import viewsets


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


class UserList(generics.ListCreateAPIView):  # new
    #  lấy danh sách tất cả người dùng
    queryset = get_user_model().objects.all()
    # chuyển đổi các thuộc tính của người dùng thành đối tượng JSON.
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
