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
    # prefetch_related cho phép bạn truy vấn các bản ghi liên kết với mô hình hiện tại trong cùng một lần truy vấn.
    # tất cả các đánh giá cho mỗi tác giả trong một lần
    # cho mối quan hệ many to many
    # =>  giúp tiết kiệm các lần truy vấn đến cơ sở dữ liệu và giúp trang web hoạt động nhanh hơn
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )

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
    # get_queryset là một phương thức trong lớp ListView
    # thay đổi cách lấy danh sách các object hoặc thêm các điều kiện lọc cho danh sách
    def get_queryset(self):
        # được sử dụng để lấy giá trị của tham số q trong query string của URL.
        # Ví dụ, nếu URL là http://example.com?q=abc, thì query sẽ là "abc".
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
