# Use 'alpha', 'beta', 'rc' or 'final' as the 4th element to indicate release type.
VERSION = (3, 2, 0, "final")


def get_short_version():
    return "%s.%s" % (VERSION[0], VERSION[1])


def get_version():
    version = "%s.%s" % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = "%s.%s" % (version, VERSION[2])
    elif VERSION[3] != "final":
        mapping = {"alpha": "a", "beta": "b", "rc": "c"}
        version = "%s%s" % (version, mapping[VERSION[3]])
        if len(VERSION) == 5:
            version = "%s%s" % (version, VERSION[4])
    return version


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
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
    # 3rd-party apps that shop depends on
    "widget_tweaks",
    "haystack",
    "treebeard",
    "django_tables2",
]


default_app_config = "shop.config.Shop"
