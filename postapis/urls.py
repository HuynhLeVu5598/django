from django.urls import path
from .views import PostListAPI, PostDetailAPI
from .views import PostList, PostDetail, UserList, UserDetail  # new

# Routers làm việc trực tiếp với các Viewsets để tự động tạo các mẫu URL
# SimpleRouter là một loại Router cung cấp một cách đơn giản để xây dựng các API bằng cách tự động tạo ra các URL cho tất cả các phương thức HTTP trong Viewset.
# Ví dụ, nếu bạn có một lớp Viewset với phương thức list() và create(),
# SimpleRouter sẽ tự động tạo ra các URL cho phương thức GET và POST

# DefaultRouter là một loại Router mạnh hơn so với SimpleRouter,
# nó cung cấp các tính năng tương tự nhưng còn cung cấp các URL cho các phương thức HTTP khác nhau như update() và destroy() cho các đối tượng có sẵn.
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")
urlpatterns = router.urls

urlpatterns = [
    path("<int:pk>/", PostDetailAPI.as_view(), name="post_detail_api"),
    path("", PostListAPI.as_view(), name="post_list_api"),
    path("users/", UserList.as_view()),  # new
    path("users/<int:pk>/", UserDetail.as_view()),  # new
]
