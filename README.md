# Kỹ Thuật Lập Trình / Project Cuối Kỳ



## Library Management System
Chương trình quản lý thư viện

## Yêu cầu

Các thư viện (package) yêu cầu để chạy chương trình
- Pandas
- PyQT5
- Openpyxl (có thể có hoặc không)

Nếu chưa có các thư viện (package) trên, có thể tải xuống qua pip
(tìm hiểu rõ hơn về [pip](https://pypi.org/project/pip/))
```
pip install PyQt5
```
```
pip install pandas
```
```
pip install openpyxl
```

## Khởi chạy chương trình

Chương trình được chạy trực tiếp ở file main.py
- Lưu ý: nếu sử dụng Pycharm (hay IDE khác), hãy đặt config đúng để chương trình chạy thuận lợi
- Ví dụ với Pycharm, hãy đặt config bên cạnh nút Run thành "Current File" khi đang ở file main.py để chạy chương trình

## Một số lỗi có thể gặp

- Lỗi đường dẫn tới file dữ liệu -> Hãy kiểm tra lại đường dẫn và sửa tại các hàm read_excel
- Lỗi chương trình tự kết thúc -> Hãy đảm bảo không mở file dữ liệu khi thực hiện các tác vụ thêm sửa xóa sách
- Lỗi không hiện ra giao diện menu -> Hãy kiểm tra config để chạy đã đúng chưa, kiểm tra có đang chạy chương trình khác không, ...