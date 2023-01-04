from django.urls import path
from .views import PostListAPI, PostDetailAPI
urlpatterns = [
    path("<int:pk>/", PostDetailAPI.as_view(), name="post_detail_api"),
    path("", PostListAPI.as_view(), name="post_list_api"),
]
