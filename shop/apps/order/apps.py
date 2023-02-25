from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class OrderConfig(ShopConfig):
    label = "order"
    name = "shop.apps.order"
    verbose_name = _("Order")
