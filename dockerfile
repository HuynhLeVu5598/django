# Image cơ sở
FROM python:3.10.8-slim-bullseye
# Set environment variables
# Tắt kiểm tra phiên bản của gói python
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# tắt việc tạo ra các tệp .pyc(tệp nhị nhân được tạo ra trong quá 
# trình biên dịch mã Python) để giảm bộ nhớ
ENV PYTHONDONTWRITEBYTECODE 1
# tắt bộ đệm (được tạo ra trước khi print) xuất ra (stdout) trong Python.
ENV PYTHONUNBUFFERED 1
# Đặt thư mục làm việc hiện tại của container Docker
WORKDIR /code
# sao chép tệp hoặc thư mục từ máy host vào container Docker
# COPY [source] [destination]
COPY ./requirements.txt .
# thực hiện các lệnh trên container Docker.
# RUN [command]
RUN pip install -r requirements.txt
# Copy project
COPY . .