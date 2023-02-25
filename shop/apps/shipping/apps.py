from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class ShippingConfig(ShopConfig):
    label = "shipping"
    name = "shop.apps.shipping"
    verbose_name = _("Shipping")
