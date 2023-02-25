from shop.apps.customer import abstract_models
from shop.core.loading import is_model_registered

__all__ = []


if not is_model_registered("customer", "ProductAlert"):

    class ProductAlert(abstract_models.AbstractProductAlert):
        pass

    __all__.append("ProductAlert")
