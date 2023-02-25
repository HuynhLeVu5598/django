from urllib.parse import quote

from django.contrib import messages
from django.core.paginator import InvalidPage
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, TemplateView

from shop.apps.catalogue.signals import product_viewed
from shop.core.loading import get_class, get_model

from django.core.paginator import Paginator

Product = get_model("catalogue", "product")
Category = get_model("catalogue", "category")
ProductAlert = get_model("customer", "ProductAlert")
ProductAlertForm = get_class("customer.forms", "ProductAlertForm")
get_product_search_handler_class = get_class(
    "catalogue.search_handlers", "get_product_search_handler_class"
)


class ProductDetailView(DetailView):
    context_object_name = "product"
    model = Product
    view_signal = product_viewed
    template_folder = "catalogue"

    # Whether to redirect to the URL with the right path
    enforce_paths = True

    # Whether to redirect child products to their parent's URL. If it's disabled,
    # we display variant product details on the separate page. Otherwise, details
    # displayed on parent product page.
    enforce_parent = False

    def get(self, request, **kwargs):
        """
        Ensures that the correct URL is used before rendering a response
        """
        self.object = product = self.get_object()

        redirect = self.redirect_if_necessary(request.path, product)
        if redirect is not None:
            return redirect

        # Do allow staff members so they can test layout etc.
        if not self.is_viewable(product, request):
            raise Http404()

        response = super().get(request, **kwargs)
        self.send_signal(request, response, product)
        return response

    def is_viewable(self, product, request):
        return product.is_public or request.user.is_staff

    def get_object(self, queryset=None):
        # Check if self.object is already set to prevent unnecessary DB calls
        if hasattr(self, "object"):
            return self.object
        else:
            return super().get_object(queryset)

    def redirect_if_necessary(self, current_path, product):
        if self.enforce_parent and product.is_child:
            return HttpResponsePermanentRedirect(product.parent.get_absolute_url())

        if self.enforce_paths:
            expected_path = product.get_absolute_url()
            if expected_path != quote(current_path):
                return HttpResponsePermanentRedirect(expected_path)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["alert_form"] = self.get_alert_form()
        ctx["has_active_alert"] = self.get_alert_status()
        return ctx

    def get_alert_status(self):
        # Check if this user already have an alert for this product
        has_alert = False
        if self.request.user.is_authenticated:
            alerts = ProductAlert.objects.filter(
                product=self.object, user=self.request.user, status=ProductAlert.ACTIVE
            )
            has_alert = alerts.exists()
        return has_alert

    def get_alert_form(self):
        return ProductAlertForm(user=self.request.user, product=self.object)

    def send_signal(self, request, response, product):
        self.view_signal.send(
            sender=self,
            product=product,
            user=request.user,
            request=request,
            response=response,
        )

    def get_template_names(self):
        """
        Return a list of possible templates.

        If an overriding class sets a template name, we use that. Otherwise,
        we try 2 options before defaulting to :file:`catalogue/detail.html`:

            1. :file:`detail-for-upc-{upc}.html`
            2. :file:`detail-for-class-{classname}.html`

        This allows alternative templates to be provided for a per-product
        and a per-item-class basis.
        """
        if self.template_name:
            return [self.template_name]

        return [
            "shop/%s/detail-for-upc-%s.html" % (self.template_folder, self.object.upc),
            "shop/%s/detail-for-class-%s.html"
            % (self.template_folder, self.object.get_product_class().slug),
            "shop/%s/detail.html" % self.template_folder,
        ]


class CatalogueView(TemplateView):
    """
    Browse all products in the catalogue
    """

    context_object_name = "products"
    template_name = "shop/catalogue/browse.html"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        try:

            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), []
            )
            response = super().get(request, *args, **kwargs)
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, _("The given page number was invalid."))
            return redirect("catalogue:index")
        return response

    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     ctx = {}
    #     ctx["summary"] = _("All products")
    #     search_context = self.search_handler.get_search_context_data(
    #         self.context_object_name
    #     )
    #     ctx.update(search_context)
    #     return ctx

    def get_queryset(self):
        # return all products
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["summary"] = _("All products")

        context["products"] = Product.objects.all()

        paginator = Paginator(context["products"], 10)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["products"] = page_obj

        return context

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx["protype"] = Category.objects.get(pk=1)

    #     ctx["summary"] = _("All products")
    #     search_context = self.search_handler.get_search_context_data(
    #         self.context_object_name
    #     )
    #     ctx.update(search_context)
    #     # Add the products variable to the context
    #     products = self.get_queryset()
    #     paginator = Paginator(products, self.paginate_by)
    #     page_number = self.request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #     ctx["products"] = page_obj

    #     return ctx

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx["category"] = self.category
    #     ctx["summary"] = self.category.name
    #     search_context = self.search_handler.get_search_context_data("products")
    #     ctx.update(search_context)
    #     products = self.get_queryset_category()
    #     paginator = Paginator(products, self.paginate_by)
    #     page_number = self.request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #     ctx["products"] = page_obj
    #     return ctx

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     category = get_object_or_404(Category, category_id=kwargs["category_id"])
    #     products = category.product_set.all()
    #     ctx["category"] = category
    #     ctx["products"] = products
    #     search_context = self.search_handler.get_search_context_data("products")
    #     ctx.update(search_context)
    #     products = self.get_queryset_category()
    #     paginator = Paginator(products, self.paginate_by)
    #     page_number = self.request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #     ctx["products"] = page_obj
    #     return ctx

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["summary"] = _("All products")

    #     if False:

    #         context["category1"] = self.category
    #         context["products"] = Product.objects.filter(categories=context["category"])
    #         print("abc ", context["products"])

    #     else:
    #         context["products"] = Product.objects.all()

    #     # Use a Paginator to limit the number of products per page
    #     paginator = Paginator(context["products"], 10)  # Show 10 products per page
    #     page_number = self.request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)

    #     context["products"] = page_obj

    #     return context

    # def get_context_data(self, **kwargs):
    #     print(kwargs)  # print the kwargs dictionary
    #     context = super().get_context_data(**kwargs)
    #     context["summary"] = _("All products")
    #     # category = Category.objects.get(id=1)
    #     # products = Product.objects.filter(categories=category)
    #     if category_slug:
    #         context["category"] = get_object_or_404(Category, slug=category_slug)
    #         context["products"] = Product.objects.filter(categories=context["category"])
    #         print(context["products"])  # print the queryset

    #     else:
    #         context["products"] = Product.objects.all()
    #     paginator = Paginator(context["products"], 10)  # Show 10 products per page
    #     page_number = self.request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)

    #     context["products"] = page_obj

    #     return context


# from django.views.generic import TemplateView
# from django.core.paginator import Paginator
# from django.utils.translation import gettext_lazy as _
# from myapp.models import Product, Category


# class CategoryView(TemplateView):
#     template_name = "myapp/category.html"
#     paginate_by = 10

#     def get(self, request, *args, **kwargs):
#         try:
#             self.category = Category.objects.get(slug=kwargs["slug"])
#             self.search_handler = self.get_search_handler(
#                 self.request.GET, request.get_full_path(), self.category
#             )
#             response = super().get(request, *args, **kwargs)
#         except Category.DoesNotExist:
#             return redirect("home")
#         except InvalidPage:
#             messages.error(request, _("The given page number was invalid."))
#             return redirect("category", slug=kwargs["slug"])
#         return response

#     def get_search_handler(self, *args, **kwargs):
#         return get_product_search_handler_class()(*args, **kwargs)

#     def get_queryset(self):
#         queryset = Product.objects.filter(categories=self.category)
#         return queryset

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx["category"] = self.category
#         ctx["summary"] = self.category.name
#         search_context = self.search_handler.get_search_context_data("products")
#         ctx.update(search_context)
#         products = self.get_queryset()
#         paginator = Paginator(products, self.paginate_by)
#         page_number = self.request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         ctx["products"] = page_obj
#         return ctx


# from django.core.paginator import Paginator
# from django.utils.translation import gettext_lazy as _
# from django.views.generic import ListView
# from .models import Product


# class ProductListView(ListView):
#     model = Product
#     context_object_name = "products"
#     template_name = "product_list.html"
#     paginate_by = 10

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx["summary"] = _("All products")
#         search_context = self.search_handler.get_search_context_data(
#             self.context_object_name
#         )
#         ctx.update(search_context)
#         # Add the products variable to the context
#         products = self.get_queryset()
#         paginator = Paginator(products, self.paginate_by)
#         page_number = self.request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         ctx["products"] = page_obj
#         return ctx


# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         "products": products,
#     }
#     return render(request, "product_list.html", context)

# from django.core.paginator import Paginator
# from django.shortcuts import render
# from .models import Product

# def product_list(request):
#     products = Product.objects.all()
#     paginator = Paginator(products, 10) # 10 products per page
#     page = request.GET.get('page')
#     products = paginator.get_page(page)
#     context = {
#         'products': products,
#     }
#     return render(request, 'product_list.html', context)


class ProductCategoryView(TemplateView):
    """
    Browse products in a given category
    """

    context_object_name = "products"
    template_name = "shop/catalogue/category.html"
    enforce_paths = True

    def get(self, request, *args, **kwargs):
        # Fetch the category; return 404 or redirect as needed
        self.category = self.get_category()

        # Allow staff members so they can test layout etc.
        if not self.is_viewable(self.category, request):
            raise Http404()

        potential_redirect = self.redirect_if_necessary(request.path, self.category)
        if potential_redirect is not None:
            return potential_redirect

        try:
            self.search_handler = self.get_search_handler(
                request.GET, request.get_full_path(), self.get_categories()
            )
            response = super().get(request, *args, **kwargs)
        except InvalidPage:
            messages.error(request, _("The given page number was invalid."))
            return redirect(self.category.get_absolute_url())

        return response

    def is_viewable(self, category, request):
        return category.is_public or request.user.is_staff

    def get_category(self):
        return get_object_or_404(Category, pk=self.kwargs["pk"])

    def redirect_if_necessary(self, current_path, category):
        if self.enforce_paths:
            # Categories are fetched by primary key to allow slug changes.
            # If the slug has changed, issue a redirect.
            expected_path = category.get_absolute_url()
            if expected_path != quote(current_path):
                return HttpResponsePermanentRedirect(expected_path)

    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    def get_categories(self):
        """
        Return a list of the current category and its ancestors
        """
        return self.category.get_descendants_and_self()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name
        )
        context.update(search_context)
        return context
