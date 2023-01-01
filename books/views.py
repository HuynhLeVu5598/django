from django.shortcuts import render
from .models import Book

# ListView liệt kê nội dung của mô hình cơ sở dữ liệu
from django.views.generic import ListView, DetailView

from django.db.models import Q

# Create your views here.


from django.contrib.auth.mixins import (
    LoginRequiredMixin,  # hạn chế quyền truy cập chỉ cho phép người dùng đã đăng nhập
    PermissionRequiredMixin,  # quyền tùy chỉnh
)


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    # xác định tên của biến mà danh sách các đối tượng được trả về sẽ được gắn vào context của template
    # mặc định là object_list
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    # chuyển hướng người dùng đến trang đăng nhập
    # "account_login" là tên định danh (slug) của trang đăng nhập
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    # mặc định là object
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"  # chỉ định quyền mong muốn

    # hàm handle_no_permission là một phương thức của lớp Django's PermissionDenied exception
    # xử lý khi người dùng không có quyền truy cập
    def handle_no_permission(self):
        return render(
            self.request,
            "books/error_page.html",
        )


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    #  QuerySet được sử dụng để lọc kết quả từ một mô hình cơ sở dữ liệu
    #  contains (phân biệt chữ hoa chữ thường)
    #  icontains (không phân biệt chữ hoa chữ thường)
    # queryset = Book.objects.filter(title__icontains="beginners")

    # sử dụng Q nếu muốn muốn tra cứu phức tạp hơn
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
