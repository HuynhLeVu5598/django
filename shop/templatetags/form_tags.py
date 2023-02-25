import warnings

from django import template
from django.template.base import TextNode

from shop.utils.deprecation import RemovedInShop32Warning

register = template.Library()


@register.tag
def annotate_form_field(parser, token):
    """
    Used to set an attribute on a form field with the widget type. This is now
    done by Django itself.
    """
    warnings.warn(
        "The annotate_form_field template tag is deprecated and will be removed in the next version of django-shop",
        RemovedInShop32Warning,
        stacklevel=2,
    )
    return TextNode("")
