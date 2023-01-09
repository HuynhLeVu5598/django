from django.urls import path, include
from .views import ListTodo, DetailTodo

from .views import BookAPIView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list_api"),
    path("todo/", ListTodo.as_view(), name="todo_list_api"),
    path("todo/<int:pk>/", DetailTodo.as_view(), name="todo_detail_api"),
    path("post/", include("postapis.urls")),
    path("post/dj-rest-auth/", include("dj_rest_auth.urls")),
    # Add Log In and Log Out
    path("api-auth/", include("rest_framework.urls")),
    #  phân phát lược đồ trực tiếp từ API dưới dạng một tuyến URL
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    #  View này sử dụng Redoc, một công cụ trực quan hóa tài liệu OpenAPI, để hiển thị tài liệu cho API của bạn
    # Redoc là một công cụ đơn giản, dễ sử dụng và dễ dàng tích hợp vào các dự án.
    # Nó cung cấp một giao diện trực quan dễ nhìn và có thể hiển thị các yêu cầu và phản hồi cho các API cùng với các mô tả chi tiết về các tham số.
    # Redoc cũng hỗ trợ các tính năng như xem mã nguồn JSON và YAML của tài liệu và thử nghiệm các yêu cầu trực tiếp từ trình duyệt.
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Swagger UI là một công cụ tương tự như Redoc, nhưng nó cung cấp thêm một số tính năng bổ sung như việc chỉnh sửa tài liệu trực tiếp từ trình duyệt và việc tạo các bản sao lưu cho các phiên bản khác nhau của tài liệu.
    # Swagger UI cũng có một giao diện trực quan dễ nhìn và có thể hiển thị các yêu cầu và phản hồi cho các API cùng với các mô tả chi tiết về các tham số.
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
