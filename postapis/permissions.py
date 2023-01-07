# xác nhận quyền của người dùng trong việc truy cập vào API.
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # has_permission được sử dụng để xác nhận quyền truy cập của người dùng đối với một phương thức HTTP cụ thể (ví dụ, GET, POST, PUT, DELETE).
    # Nó có một tham số là request, là một đối tượng HttpRequest, và trả về True nếu người dùng có quyền truy cập và False nếu người dùng không có quyền truy cập
    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    # has_object_permission là một method tương tự như has_permission, nhưng nó dùng để kiểm tra xem người dùng có quyền truy cập vào một object cụ thể hay không.
    def has_object_permission(self, request, view, obj):
        # cho phép yêu cầu chỉ đọc nhưng giới hạn quyền ghi đối với chỉ tác giả của bài đăng trên blog
        # kiểm tra xem phương thức HTTP có trong danh sách các phương thức an toàn không.
        # Các phương thức an toàn là các phương thức không thay đổi trạng thái của hệ thống, bao gồm: GET, HEAD, OPTIONS
        # Nếu phương thức HTTP truy vấn là một trong các phương thức trên, điều kiện sẽ trả về True.
        # Ngược lại, nếu phương thức là một trong các phương thức không an toàn,
        # như POST, PUT, DELETE, điều kiện sẽ trả về False.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
