import warnings

from shop.utils.deprecation import RemovedInShop32Warning


def deprecated(obj):
    if isinstance(obj, type):
        return _deprecated_cls(cls=obj)
    else:
        return _deprecated_func(f=obj)


def _deprecated_func(f, warn_cls=RemovedInShop32Warning):
    def _deprecated(*args, **kwargs):
        message = (
            "Method '%s' is deprecated and will be "
            "removed in the next version of django-shop" % f.__name__
        )
        warnings.warn(message, warn_cls, stacklevel=2)
        return f(*args, **kwargs)

    return _deprecated


def _deprecated_cls(cls, warn_cls=RemovedInShop32Warning):
    class Deprecated(cls):
        def __init__(self, *args, **kwargs):
            message = (
                "Class '%s' is deprecated and will be "
                "removed in the next version of django-shop" % cls.__name__
            )
            warnings.warn(message, warn_cls, stacklevel=2)
            super().__init__(*args, **kwargs)

    return Deprecated
