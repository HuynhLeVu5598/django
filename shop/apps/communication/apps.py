from django.utils.translation import gettext_lazy as _

from shop.core.application import ShopConfig


class CommunicationConfig(ShopConfig):
    label = "communication"
    name = "shop.apps.communication"
    verbose_name = _("Communication")
