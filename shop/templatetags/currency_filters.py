from decimal import Decimal as D
from decimal import InvalidOperation

from babel.numbers import format_currency
from django import template
from django.conf import settings
from django.utils.translation import get_language, to_locale

register = template.Library()


@register.filter(name="currency")
def currency(value, currency=None):
    """
    Format decimal value as currency
    """
    if currency is None:
        currency = settings.SHOP_DEFAULT_CURRENCY

    try:
        value = D(value)
    except (TypeError, InvalidOperation):
        return ""
    # Using Babel's currency formatting
    # http://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency
    SHOP_CURRENCY_FORMAT = getattr(settings, "SHOP_CURRENCY_FORMAT", None)
    kwargs = {
        "currency": currency,
        "locale": to_locale(get_language() or settings.LANGUAGE_CODE),
    }
    if isinstance(SHOP_CURRENCY_FORMAT, dict):
        kwargs.update(SHOP_CURRENCY_FORMAT.get(currency, {}))
    else:
        kwargs["format"] = SHOP_CURRENCY_FORMAT
    return format_currency(value, **kwargs)
