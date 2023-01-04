from django.urls import path, include
from .views import ListTodo, DetailTodo

from .views import BookAPIView
urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list_api"),
    path("todo/", ListTodo.as_view(), name="todo_list_api"),
    path("todo/<int:pk>/", DetailTodo.as_view(), name="todo_detail_api"),
    path("post/", include("postapis.urls")),
    path("api-auth/", include("rest_framework.urls")),

]
