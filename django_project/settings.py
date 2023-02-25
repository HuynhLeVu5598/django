"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from environs import Env
import socket

# from cloth.defaults import *
from shop.defaults import *


env = Env()
env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#  tên host, tên alias và danh sách địa chỉ IP của máy tính hiện tại.
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# danh sách các địa chỉ IP nội bộ được tạo bằng cách lấy từng phần tử trong danh sách ips và thêm ký tự "1" vào cuối
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
# => đảm bảo rằng INTERNAL_IPS phù hợp với máy chủ Docker

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-z!)c6ob_xlaok234hu*_$!qghek48*i6(uc*7uo2^xv)15vr=b"
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG = env.bool("DJANGO_DEBUG")
DEBUG = env.bool("DJANGO_DEBUG", default=False)

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

# xác định số giây mà trình duyệt sẽ yêu cầu một kết nối SSL cho trang web. Nếu giá trị là 0, thẻ HSTS sẽ không được sử dụng.
# được đặt thành 0 theo mặc định nhưng càng lớn càng tốt cho mục đích bảo mật
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)  # 30 days
# buộc các tên miền phụ sử dụng SSL, sẽ đặt nó thành True trong sản xuất.
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
# yêu cầu trình duyệt sử dụng SSL cho trang web trước khi trang web đó được yêu cầu
# chỉ có tác dụng khi SECURE_HSTS_SECONDS # 0
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

# Nếu đặt là True, cookie phiên đăng nhập sẽ chỉ được gửi qua một kết nối HTTPS an toàn.
# Nếu đặt là False, cookie có thể được gửi qua một kết nối HTTP không an toàn.
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
# Nếu đặt là True, cookie bảo vệ CSRF sẽ chỉ được gửi qua một kết nối HTTPS an toàn.
# Nếu đặt là False, cookie có thể được gửi qua một kết nối HTTP không an toàn.
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]


# Application definition
# Lệnh migrate sẽ chỉ chạy migrations cho các ứng dụng trong INSTALLED_APPS.
INSTALLED_APPS = [
    # Trang quản trị
    "django.contrib.admin",
    # Một hệ thống xác thực.
    "django.contrib.auth",
    # Một khuôn khổ cho các loại nội dung.
    "django.contrib.contenttypes",
    # Một khung phiên.
    "django.contrib.sessions",
    # Một khung nhắn tin.
    "django.contrib.messages",
    # Một khuôn khổ để quản lý các tập tin tĩnh.
    "django.contrib.staticfiles",
    # thư viện mạnh mẽ được sử dụng để xây dựng các API
    "rest_framework",
    # cho phép khách hàng xác định xem có nên cho phép các yêu cầu tên miền chéo hay không và khi nào
    # xử lý các yêu cầu gửi đến server từ một domain khác
    "corsheaders",
    # xử lý tệp tĩnh trên các nền tảng hosting
    "whitenoise.runserver_nostatic",
    # Django Crispy Forms là một thư viện mã nguồn mở cho phép bạn tạo các form HTML dễ dàng hơn trong Django
    "crispy_forms",
    "crispy_bootstrap5",
    #  quản lý nhiều trang web trên cùng một hệ thống
    # giúp xác định xem một người dùng đang truy cập trang web nào trong hệ thống của bạn
    "django.contrib.sites",
    # Django Allauth là một công cụ mạnh mẽ cho phép bạn tích hợp đăng nhập và đăng ký qua các dịch vụ xác thực như Google, Facebook, Twitter và nhiều dịch vụ khác vào trang web của bạn
    "allauth",
    "allauth.account",
    # https://testdriven.io/blog/django-social-auth/
    # https://learndjango.com/tutorials/django-allauth-tutorial
    # nếu gặp lỗi SocialApp matching query does not exist: https://stackoverflow.com/questions/15409366/django-socialapp-matching-query-does-not-exist
    "allauth.socialaccount",
    # social providers
    "allauth.socialaccount.providers.github",
    # "allauth.socialaccount.providers.twitter",
    #  tối ưu hóa các truy vấn cơ sở dữ liệu
    "debug_toolbar",
    # Sử dụng lớp cấu hình mặc định của ứng dụng
    "pages",
    "books",
    "apis",
    "postapis",
    "polls",
    "foods",
    # Sử dụng lớp cấu hình riêng của bạn cho ứng dụng
    "accounts.apps.AccountsConfig",
    # Font Awesome
    # https://fontawesome.com/docs/web/use-with/python-django
    "fontawesomefree",
    "rest_framework.authtoken",  # new
    # là một package trong Django cho phép bạn xây dựng các API RESTful cho việc đăng nhập, đăng ký, quên mật khẩu và các tác vụ liên quan khác.
    "dj_rest_auth",  # new
    # DRF Spectacular là một công cụ hỗ trợ cho Django REST framework (DRF) cho phép bạn tạo ra tài liệu API động trong dạng HTML
    "drf_spectacular",
    # các trường để có giao diện đẹp hơn
    "markdownx",
    # handle duration field in the form
    "durationwidget",
    "django.contrib.flatpages",
    # "cloth.config.Shop",
    # "cloth.apps.analytics.apps.AnalyticsConfig",
    # "cloth.apps.checkout.apps.CheckoutConfig",
    # "cloth.apps.address.apps.AddressConfig",
    # "cloth.apps.shipping.apps.ShippingConfig",
    # "cloth.apps.catalogue.apps.CatalogueConfig",
    # "cloth.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    # "cloth.apps.communication.apps.CommunicationConfig",
    # "cloth.apps.partner.apps.PartnerConfig",
    # "cloth.apps.basket.apps.BasketConfig",
    # "cloth.apps.payment.apps.PaymentConfig",
    # "cloth.apps.offer.apps.OfferConfig",
    # "cloth.apps.order.apps.OrderConfig",
    # "cloth.apps.customer.apps.CustomerConfig",
    # "cloth.apps.search.apps.SearchConfig",
    # "cloth.apps.voucher.apps.VoucherConfig",
    # "cloth.apps.wishlists.apps.WishlistsConfig",
    # "cloth.apps.dashboard.apps.DashboardConfig",
    # "cloth.apps.dashboard.reports.apps.ReportsDashboardConfig",
    # "cloth.apps.dashboard.users.apps.UsersDashboardConfig",
    # "cloth.apps.dashboard.orders.apps.OrdersDashboardConfig",
    # "cloth.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    # "cloth.apps.dashboard.offers.apps.OffersDashboardConfig",
    # "cloth.apps.dashboard.partners.apps.PartnersDashboardConfig",
    # "cloth.apps.dashboard.pages.apps.PagesDashboardConfig",
    # "cloth.apps.dashboard.ranges.apps.RangesDashboardConfig",
    # "cloth.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    # "cloth.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    # "cloth.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    # "cloth.apps.dashboard.shipping.apps.ShippingDashboardConfig",
    "shop.config.Shop",
    "shop.apps.analytics.apps.AnalyticsConfig",
    "shop.apps.checkout.apps.CheckoutConfig",
    "shop.apps.address.apps.AddressConfig",
    "shop.apps.shipping.apps.ShippingConfig",
    "shop.apps.catalogue.apps.CatalogueConfig",
    "shop.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    "shop.apps.communication.apps.CommunicationConfig",
    "shop.apps.partner.apps.PartnerConfig",
    "shop.apps.basket.apps.BasketConfig",
    "shop.apps.payment.apps.PaymentConfig",
    "shop.apps.offer.apps.OfferConfig",
    "shop.apps.order.apps.OrderConfig",
    "shop.apps.customer.apps.CustomerConfig",
    "shop.apps.search.apps.SearchConfig",
    "shop.apps.voucher.apps.VoucherConfig",
    "shop.apps.wishlists.apps.WishlistsConfig",
    "shop.apps.dashboard.apps.DashboardConfig",
    "shop.apps.dashboard.reports.apps.ReportsDashboardConfig",
    "shop.apps.dashboard.users.apps.UsersDashboardConfig",
    "shop.apps.dashboard.orders.apps.OrdersDashboardConfig",
    "shop.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    "shop.apps.dashboard.offers.apps.OffersDashboardConfig",
    "shop.apps.dashboard.partners.apps.PartnersDashboardConfig",
    "shop.apps.dashboard.pages.apps.PagesDashboardConfig",
    "shop.apps.dashboard.ranges.apps.RangesDashboardConfig",
    "shop.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    "shop.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    "shop.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    "shop.apps.dashboard.shipping.apps.ShippingDashboardConfig",
    # 3rd-party apps that cloth depends on
    "widget_tweaks",
    "haystack",
    "treebeard",
    "sorl.thumbnail",  # Default thumbnail backend, can be replaced
    "django_tables2",
]

# REST_FRAMEWORK cấu hình các tùy chọn cho API
# bao gồm cách thức xác thực và lập lịch cho API, cách thức sử dụng phân trang, bảo mật và cách thức sử dụng các serializer
REST_FRAMEWORK = {
    # định nghĩa một lớp quyền mặc định sẽ được sử dụng cho toàn bộ các ViewSet của dự án
    "DEFAULT_PERMISSION_CLASSES": [
        # bất kỳ người dùng nào, được xác thực hay không, đều có toàn quyền truy cập
        # "rest_framework.permissions.AllowAny",
        # chỉ người dùng đã đăng ký có quyền truy cập
        "rest_framework.permissions.IsAuthenticated",
        # chỉ quản trị viên/siêu người dùng mới có quyền truy cập
        # "rest_framework.permissions.IsAdminUser",
        # người dùng trái phép có thể xem bất kỳ trang nào, nhưng chỉ người dùng được xác thực mới có đặc quyền viết, chỉnh sửa hoặc xóa
        # "rest_framework.permissions.IsAuthenticatedOrReadOnly ",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [  # new
        # nếu client gửi một yêu cầu bằng một trong các phương thức "SAFE_METHODS" (GET, HEAD, OPTIONS),
        # thì Rest Framework sẽ cho phép yêu cầu đó thông qua mà không yêu cầu xác thực người dùng.
        # "SessionAuthentication" là một lớp xác thực sử dụng cookie để xác thực người dùng
        "rest_framework.authentication.SessionAuthentication",
        # "BasicAuthentication" là một lớp xác thực sử dụng HTTP Basic Auth để xác thực người dùng.
        # "rest_framework.authentication.BasicAuthentication",
        # TokenAuthentication là một trong các phương thức xác thực mà Django REST framework hỗ trợ.
        #  Nó sử dụng một token để xác thực người dùng trên mỗi yêu cầu.
        # Token có thể được lưu trữ trong cookie hoặc trong trình duyệt để lưu lại đăng nhập người dùng
        "rest_framework.authentication.TokenAuthentication",  # new
    ],
    # Thiết lập này xác định kiểu schema sẽ được sử dụng mặc định cho các API.
    # AutoSchema là một lớp cho phép tự động tạo ra các tài liệu OpenAPI từ các view và serializers của Django REST framework.
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# là một tập hợp các thiết lập cho Django REST framework (DRF) Spectacular, một thư viện giúp tạo tài liệu OpenAPI cho các API Django.
# Trong trường hợp cụ thể, các thiết lập này định nghĩa các thông tin cơ bản về dự án API, bao gồm tiêu đề, mô tả và phiên bản.
SPECTACULAR_SETTINGS = {
    "TITLE": "Blog API Project",
    "DESCRIPTION": "A sample blog to learn about DRF",
    "VERSION": "1.0.0",
    # OTHER SETTINGS
    # như địa chỉ URL của tài liệu, ngôn ngữ sử dụng, ...
}

# django-crispy-forms
# xác định các bộ template mà bạn muốn sử dụng
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
# xác định bộ template mà bạn muốn sử dụng mặc định cho toàn bộ form trong ứng dụng của bạn
CRISPY_TEMPLATE_PACK = "bootstrap5"


AUTHENTICATION_BACKENDS = (
    # xác thực một người dùng
    "django.contrib.auth.backends.ModelBackend",
    # xác thực cụ thể (đăng nhập qua e-mail)
    "allauth.account.auth_backends.AuthenticationBackend",
    # "cloth.apps.customer.auth_backends.EmailBackend",
    "shop.apps.customer.auth_backends.EmailBackend",
)


HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.simple_backend.SimpleEngine",
    },
}

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.solr_backend.SolrEngine",
        "URL": "http://localhost:8983/solr",
        "INCLUDE_SPELLING": True,
    },
}

# ID của trang web mà bạn đang xây dựng trong hệ thống các trang web của mình.
SITE_ID = 1

# django-allauth config
# tùy chọn hộp “Remember Me” sẽ đặt thành True và không hiển thị
ACCOUNT_SESSION_REMEMBER = True
#  chỉ yêu cầu mật khẩu một lần khi đăng ký
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# chỉ đăng nhập bằng email
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
# điều hướng đến "home" khi đăng nhập thành công
LOGIN_REDIRECT_URL = "home"
# điều hướng đến "home" khi đăng xuất thành công
ACCOUNT_LOGOUT_REDIRECT_URL = "home"


# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {
    # form nhập email khi quên mật khẩu
    "reset_password": "accounts.forms.CustomPasswordResetForm",
    # đổi mật khẩu
    "change_password": "accounts.forms.CustomPasswordChangeForm",
    # url đổi mk khi quên mật khẩu
    "reset_password_from_key": "accounts.forms.CustomResetPasswordKeyForm",
}

# ACCOUNT_FORMS = {
#     'login': 'allauth.account.forms.LoginForm',
#     'signup': 'allauth.account.forms.SignupForm',
#     'add_email': 'allauth.account.forms.AddEmailForm',
#     'change_password': 'allauth.account.forms.ChangePasswordForm',
#     'set_password': 'allauth.account.forms.SetPasswordForm',
#     'reset_password': 'allauth.account.forms.ResetPasswordForm',
#     'reset_password_from_key':
#     'allauth.account.forms.ResetPasswordKeyForm',
#     'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
# }
# ACCOUNT_PASSWORD_CHANGE_FORM_CLASS = 'accounts.forms.CustomPasswordChangeForm'
# ACCOUNT_PASSWORD_RESET_TEMPLATE_NAME = "account/password_reset_form.html"
# ACCOUNT_FORGOT_PASSWORD_TEMPLATE_NAME = "account/password_reset_form.html"
# ACCOUNT_EMAIL_TEMPLATE_NAME = "password_reset.html"


# yêu cầu Django xuất bất kỳ email nào tới bảng điều khiển dòng lệnh
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# dịch vụ thư điện tử smtp
# trang sendgrip.com đang lỗi

DEBUG = env.bool("DJANGO_DEBUG", default=False)

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "APP": {
            "client_id": env("GITHUB_CLIENT_ID"),
            "secret": env("GITHUB_API_SECRET"),
            "key": env("GITHUB_APP_KEY"),
        }
    },
    "VERIFIED_EMAIL": True,
}

# SOCIALACCOUNT_PROVIDERS = {
#     "facebook": {
#         "CLIENT_ID": "<your-client-id>",
#         "SECRET_KEY": "<your-secret-key>",
#     },
#     "google": {
#         "CLIENT_ID": "<your-client-id>",
#         "SECRET_KEY": "<your-secret-key>",
#     },
# }


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # lấy các yêu cầu từ bộ nhớ cache của hệ thống
    # Nếu có một yêu cầu đã được lưu trữ trong cache, middleware sẽ trả về câu trả lời từ cache và không gửi yêu cầu đến server
    # giúp giảm đáng kể thời gian xử lý yêu cầu và tăng tốc độ truy cập cho người dùng
    "django.middleware.cache.FetchFromCacheMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # "cloth.apps.basket.middleware.BasketMiddleware",
    "shop.apps.basket.middleware.BasketMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
]

#  danh sách các tên miền hoặc địa chỉ IP được cho phép gửi yêu cầu tới server
CORS_ALLOWED_ORIGINS = (
    # cổng mặc định cho React (nếu đó là giao diện người dùng đang được sử dụng)
    "http://localhost:3000",
    # cổng Django mặc định.
    "http://localhost:8000",
)

#  giao diện người dùng React chuyên dụng, tính năng bảo vệ CSRF không có sẵn
# được sử dụng để xác định những tên miền nào được tin tưởng và có thể gửi yêu cầu với mã thông báo Cross-Site Request Forgery (CSRF).
# Điều này có nghĩa là khi một yêu cầu đến từ một tên miền được xác định trong danh sách này, Django sẽ cho phép yêu cầu đó được xử lý mà không cần kiểm tra mã thông báo CSRF.
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

#  Tên alias của bộ nhớ cache sẽ được sử dụng cho middleware.
CACHE_MIDDLEWARE_ALIAS = "default"
# số giây để lưu trữ bộ nhớ cache
# mặc định là 1 tuần  cho trang web có nội dung không thay đổi thường xuyên
# rút ngắn thời gian nếu trang web có nội dung thay đổi thường xuyên
CACHE_MIDDLEWARE_SECONDS = 604800
# Tiền tố cho mỗi khóa bộ nhớ cache.
CACHE_MIDDLEWARE_KEY_PREFIX = ""

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "cloth.apps.search.context_processors.search_form",
                # "cloth.apps.checkout.context_processors.checkout",
                # "cloth.apps.communication.notifications.context_processors.notifications",
                # "cloth.core.context_processors.metadata",
                "shop.apps.search.context_processors.search_form",
                "shop.apps.checkout.context_processors.checkout",
                "shop.apps.communication.notifications.context_processors.notifications",
                "shop.core.context_processors.metadata",
            ],
        },
    },
]


WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgres",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "db",  # set in docker-compose.yml
#         "PORT": 5432,  # default postgres port
#     }
# }
DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres@db/postgres"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# CLOTH_INITIAL_ORDER_STATUS = "Pending"
# CLOTH_INITIAL_LINE_STATUS = "Pending"
# CLOTH_ORDER_STATUS_PIPELINE = {
#     "Pending": (
#         "Being processed",
#         "Cancelled",
#     ),
#     "Being processed": (
#         "Processed",
#         "Cancelled",
#     ),
#     "Cancelled": (),
# }


SHOP_INITIAL_ORDER_STATUS = "Pending"
SHOP_INITIAL_LINE_STATUS = "Pending"
SHOP_ORDER_STATUS_PIPELINE = {
    "Pending": (
        "Being processed",
        "Cancelled",
    ),
    "Being processed": (
        "Processed",
        "Cancelled",
    ),
    "Cancelled": (),
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"
# LANGUAGE_CODE = "vi"
# Cập nhật múi giờ
# TIME_ZONE = "UTC"
TIME_ZONE = "Asia/Ho_Chi_Minh"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
# danh sách các đường dẫn thư mục đến những tập tin tĩnh (CSS, JavaScript, hình ảnh)
# các tập tin không thay đổi theo thời gian và không có sự liên kết đến các biến hoặc dữ liệu người dùng
STATICFILES_DIRS = [BASE_DIR / "static"]

# URL có thể sử dụng trong các mẫu cho các tệp
MEDIA_URL = "/media/"
# đường dẫn hệ thống tệp tuyệt đối tới thư mục dành cho các tệp do người dùng tải lên (hình ảnh, âm thanh, video)
# có thể được thay đổi theo thời gian hoặc có sự liên kết đến các biến hoặc dữ liệu người dùng.
MEDIA_ROOT = BASE_DIR / "media"
# Một danh sách các thư mục chứa các tập tin tĩnh (static files) mà bạn muốn Django tìm kiếm
# khi bạn sử dụng các lệnh collectstatic hoặc khi sử dụng {% static %} trong các mẫu Django.
# Khi bạn muốn sử dụng máy chủ tĩnh để phân phối tập tin tĩnh của bạn
STATIC_ROOT = BASE_DIR / "staticfiles"
# chuỗi cấu hình cho lớp cung cấp lưu trữ tĩnh
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
# xử lý và phân phối tệp tĩnh trên web. Nó hỗ trợ nén và tối ưu hóa tệp tĩnh, giúp trang web của bạn tải nhanh hơn.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# một biến toàn cục trong Django, được sử dụng để xác định model nào sẽ được sử dụng làm model người dùng trong hệ thống
AUTH_USER_MODEL = "accounts.CustomUser"

DEFAULT_FROM_EMAIL = "huynhlevu55981@gmail.com"
