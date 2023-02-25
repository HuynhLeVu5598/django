from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class VoucherConfig(ShopConfig):
    label = "voucher"
    name = "shop.apps.voucher"
    verbose_name = _("Voucher")

    def ready(self):
        from . import receivers  # noqa
