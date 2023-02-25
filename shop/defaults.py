from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

SHOP_SHOP_NAME = "Shop"
SHOP_SHOP_TAGLINE = ""
SHOP_HOMEPAGE = reverse_lazy("catalogue:index")

# Dynamic class loading
SHOP_DYNAMIC_CLASS_LOADER = "shop.core.loading.default_class_loader"

# Basket settings
SHOP_BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
SHOP_BASKET_COOKIE_OPEN = "shop_open_basket"
SHOP_BASKET_COOKIE_SECURE = False
SHOP_MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Recently-viewed products
SHOP_RECENTLY_VIEWED_COOKIE_LIFETIME = 7 * 24 * 60 * 60
SHOP_RECENTLY_VIEWED_COOKIE_NAME = "shop_history"
SHOP_RECENTLY_VIEWED_COOKIE_SECURE = False
SHOP_RECENTLY_VIEWED_PRODUCTS = 20

# Currency
SHOP_DEFAULT_CURRENCY = "GBP"

# Paths
SHOP_IMAGE_FOLDER = "images/products/%Y/%m/"
SHOP_DELETE_IMAGE_FILES = True

# Copy this image from shop/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
SHOP_MISSING_IMAGE_URL = "image_not_found.jpg"

# Address settings
SHOP_REQUIRED_ADDRESS_FIELDS = (
    "first_name",
    "last_name",
    "line1",
    "line4",
    "postcode",
    "country",
)

# Pagination settings

SHOP_OFFERS_PER_PAGE = 20
SHOP_PRODUCTS_PER_PAGE = 20
SHOP_REVIEWS_PER_PAGE = 20
SHOP_NOTIFICATIONS_PER_PAGE = 20
SHOP_EMAILS_PER_PAGE = 20
SHOP_ORDERS_PER_PAGE = 20
SHOP_ADDRESSES_PER_PAGE = 20
SHOP_STOCK_ALERTS_PER_PAGE = 20
SHOP_DASHBOARD_ITEMS_PER_PAGE = 20

# Checkout
SHOP_ALLOW_ANON_CHECKOUT = False

# Reviews
SHOP_ALLOW_ANON_REVIEWS = True
SHOP_MODERATE_REVIEWS = False

# Accounts
SHOP_ACCOUNTS_REDIRECT_URL = "customer:profile-view"

# This enables sending alert notifications/emails instantly when products get
# back in stock by listening to stock record update signals.
# This might impact performance for large numbers of stock record updates.
# Alternatively, the management command ``shop_send_alerts`` can be used to
# run periodically, e.g. as a cron job. In this case eager alerts should be
# disabled.
SHOP_EAGER_ALERTS = True

# Registration
SHOP_SEND_REGISTRATION_EMAIL = True
SHOP_FROM_EMAIL = "shop@example.com"

# Slug handling
SHOP_SLUG_FUNCTION = "shop.core.utils.default_slugifier"
SHOP_SLUG_MAP = {}
SHOP_SLUG_BLACKLIST = []
SHOP_SLUG_ALLOW_UNICODE = False

# Cookies
SHOP_COOKIES_DELETE_ON_LOGOUT = [
    "shop_recently_viewed_products",
]

# Offers
SHOP_OFFERS_INCL_TAX = False
# Values (using the names of the model constants) from
# "offer.ConditionalOffer.TYPE_CHOICES"
SHOP_OFFERS_IMPLEMENTED_TYPES = [
    "SITE",
    "VOUCHER",
]

# Hidden Shop features, e.g. wishlists or reviews
SHOP_HIDDEN_FEATURES = []

# Menu structure of the dashboard navigation
SHOP_DASHBOARD_NAVIGATION = [
    {
        "label": _("Dashboard"),
        "icon": "fas fa-list",
        "url_name": "dashboard:index",
    },
    {
        "label": _("Catalogue"),
        "icon": "fas fa-sitemap",
        "children": [
            {
                "label": _("Products"),
                "url_name": "dashboard:catalogue-product-list",
            },
            {
                "label": _("Product Types"),
                "url_name": "dashboard:catalogue-class-list",
            },
            {
                "label": _("Categories"),
                "url_name": "dashboard:catalogue-category-list",
            },
            {
                "label": _("Ranges"),
                "url_name": "dashboard:range-list",
            },
            {
                "label": _("Low stock alerts"),
                "url_name": "dashboard:stock-alert-list",
            },
            {
                "label": _("Options"),
                "url_name": "dashboard:catalogue-option-list",
            },
        ],
    },
    {
        "label": _("Fulfilment"),
        "icon": "fas fa-shopping-cart",
        "children": [
            {
                "label": _("Orders"),
                "url_name": "dashboard:order-list",
            },
            {
                "label": _("Statistics"),
                "url_name": "dashboard:order-stats",
            },
            {
                "label": _("Partners"),
                "url_name": "dashboard:partner-list",
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ],
    },
    {
        "label": _("Customers"),
        "icon": "fas fa-users",
        "children": [
            {
                "label": _("Customers"),
                "url_name": "dashboard:users-index",
            },
            {
                "label": _("Stock alert requests"),
                "url_name": "dashboard:user-alert-list",
            },
        ],
    },
    {
        "label": _("Offers"),
        "icon": "fas fa-bullhorn",
        "children": [
            {
                "label": _("Offers"),
                "url_name": "dashboard:offer-list",
            },
            {
                "label": _("Vouchers"),
                "url_name": "dashboard:voucher-list",
            },
            {
                "label": _("Voucher Sets"),
                "url_name": "dashboard:voucher-set-list",
            },
        ],
    },
    {
        "label": _("Content"),
        "icon": "fas fa-folder",
        "children": [
            {
                "label": _("Pages"),
                "url_name": "dashboard:page-list",
            },
            {
                "label": _("Email templates"),
                "url_name": "dashboard:comms-list",
            },
            {
                "label": _("Reviews"),
                "url_name": "dashboard:reviews-list",
            },
        ],
    },
    {
        "label": _("Reports"),
        "icon": "fas fa-chart-bar",
        "url_name": "dashboard:reports-index",
    },
]
SHOP_DASHBOARD_DEFAULT_ACCESS_FUNCTION = (
    "shop.apps.dashboard.nav.default_access_fn"  # noqa
)

# Search facets
SHOP_SEARCH_FACETS = {
    "fields": {
        # The key for these dicts will be used when passing facet data
        # to the template. Same for the 'queries' dict below.
        "product_class": {"name": _("Type"), "field": "product_class"},
        "rating": {"name": _("Rating"), "field": "rating"},
        # You can specify an 'options' element that will be passed to the
        # SearchQuerySet.facet() call.
        # For instance, with Elasticsearch backend, 'options': {'order': 'term'}
        # will sort items in a facet by title instead of number of items.
        # It's hard to get 'missing' to work
        # correctly though as of Solr's hilarious syntax for selecting
        # items without a specific facet:
        # http://wiki.apache.org/solr/SimpleFacetParameters#facet.method
        # 'options': {'missing': 'true'}
    },
    "queries": {
        "price_range": {
            "name": _("Price range"),
            "field": "price",
            "queries": [
                # This is a list of (name, query) tuples where the name will
                # be displayed on the front-end.
                (_("0 to 20"), "[0 TO 20]"),
                (_("20 to 40"), "[20 TO 40]"),
                (_("40 to 60"), "[40 TO 60]"),
                (_("60+"), "[60 TO *]"),
            ],
        },
    },
}

SHOP_PRODUCT_SEARCH_HANDLER = None

SHOP_THUMBNAILER = "shop.core.thumbnails.SorlThumbnail"

SHOP_URL_SCHEMA = "http"

SHOP_SAVE_SENT_EMAILS_TO_DB = True
