from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path("", home, name="home_food"),
    path("detail/<int:id>/", detail, name="detail_food"),
    path("new/", create, name="create_food"),
    path("update/<int:id>/", update, name="update_food"),
    path("delete/<int:id>/", delete, name="delete_food"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
