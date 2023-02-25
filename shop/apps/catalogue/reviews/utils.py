from django.conf import settings

from shop.core.loading import get_model


def get_default_review_status():
    ProductReview = get_model("reviews", "ProductReview")

    if settings.SHOP_MODERATE_REVIEWS:
        return ProductReview.FOR_MODERATION

    return ProductReview.APPROVED
