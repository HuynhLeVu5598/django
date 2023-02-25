from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class PaymentConfig(ShopConfig):
    label = "payment"
    name = "shop.apps.payment"
    verbose_name = _("Payment")
