from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class PartnerConfig(ShopConfig):
    label = "partner"
    name = "shop.apps.partner"
    verbose_name = _("Partner")

    def ready(self):
        from . import receivers  # noqa
