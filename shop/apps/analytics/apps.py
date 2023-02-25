from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class AnalyticsConfig(ShopConfig):
    label = "analytics"
    name = "shop.apps.analytics"
    verbose_name = _("Analytics")

    def ready(self):
        from . import receivers  # noqa
