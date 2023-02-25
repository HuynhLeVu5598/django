from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class AddressConfig(ShopConfig):
    label = "address"
    name = "shop.apps.address"
    verbose_name = _("Address")
