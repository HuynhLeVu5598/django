"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# tạo URL cho tập tin tĩnh (static files) trong Django project
from django.conf.urls.static import static

from django.conf.urls import handler403

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

urlpatterns += [
    path("admin/", admin.site.urls),
    # chứa URL patterns cho các tính năng xác thực và quản trị người dùng trong Django
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    # path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
    path("api/", include("apis.urls")), 
]

# cho phép Django tải các tập tin từ thư mục media.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
