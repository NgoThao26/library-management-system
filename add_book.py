# Ngô Thu Thảo 20216960
import pandas as pd
import logging
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from book import Book
from util import is_book_id_exists, dataframe


class AddBookWidget(QWidget):
    """
    Giao diện thêm sách mới
    """
    def __init__(self):
        super().__init__()
        self.status_edit = None
        self.isbn_edit = None
        self.year_edit = None
        self.publisher_edit = None
        self.authors_edit = None
        self.title_edit = None
        self.book_id_edit = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setWindowTitle("THÊM SÁCH MỚI")
        layout.addWidget(QLabel("===== THÊM SÁCH MỚI ====="))

        layout.addWidget(QLabel("Mã sách"))
        self.book_id_edit = QLineEdit()
        layout.addWidget(self.book_id_edit)

        layout.addWidget(QLabel("Tên sách"))
        self.title_edit = QLineEdit()
        layout.addWidget(self.title_edit)

        layout.addWidget(QLabel("Tác giả"))
        self.authors_edit = QLineEdit()
        layout.addWidget(self.authors_edit)

        layout.addWidget(QLabel("Nhà xuất bản"))
        self.publisher_edit = QLineEdit()
        layout.addWidget(self.publisher_edit)

        layout.addWidget(QLabel("Năm xuất bản"))
        self.year_edit = QLineEdit()
        layout.addWidget(self.year_edit)

        layout.addWidget(QLabel("Số ISBN"))
        self.isbn_edit = QLineEdit()
        layout.addWidget(self.isbn_edit)

        layout.addWidget(QLabel("Trạng thái"))
        self.status_edit = QLineEdit()
        layout.addWidget(self.status_edit)

        # Tạo nút "Xác nhận" để thêm sách mới
        button_confirm = QPushButton("Xác nhận")
        button_confirm.clicked.connect(self.add_new_book)
        layout.addWidget(button_confirm)

        self.setLayout(layout)
        self.show()

    def add_new_book(self):
        # Lấy thông tin sách từ các QLineEdit
        book_id = self.book_id_edit.text()
        title = self.title_edit.text()
        authors = self.authors_edit.text()
        publisher = self.publisher_edit.text()
        year = self.year_edit.text()
        isbn = self.isbn_edit.text()
        status = self.status_edit.text()

        if book_id == '' or title == '' or authors == '':
            # kiểm tra xem mã sách, tên sách hoặc tên tác giả có để trống
            logging.warning("Mã sách, Tên sách, và Tác giả không được để trống.")
            QMessageBox.warning(self, "Cảnh báo", "Mã sách, Tên sách, và Tác giả không được để trống.")
            return

        if is_book_id_exists(book_id):
            logging.warning(f"Mã sách {book_id} đã tồn tại")
            QMessageBox.warning(self, "Cảnh báo", "Mã sách đã tồn tại. Không thêm sách mới.")
            self.ready()
            return

        new_book = Book(book_id, title, authors, publisher, year, isbn, status)
        add_book(new_book)
        logging.info(f"Đã thêm sách {book_id} thành công.")
        QMessageBox.information(self, "Thông báo", "Đã thêm sách thành công.")
        self.ready()

    def ready(self):
        """
        Đặt lại các phần để tiếp tục thêm sách khác
        :return:
        """
        self.book_id_edit.clear()
        self.title_edit.clear()
        self.authors_edit.clear()
        self.publisher_edit.clear()
        self.year_edit.clear()
        self.isbn_edit.clear()
        self.status_edit.clear()

        # Trở về lại focus vào ô nhập mã sách
        self.book_id_edit.setFocus()


def add_book(book):
    """
    Thêm sách mới
    :param book: thông tin sách mới để thêm
    :return:
    """
    df = dataframe()

    # Tạo DataFrame mới từ dữ liệu của sách mới
    new_book_data = {
        'Mã sách': [book.bookID],
        'Tên sách': [book.title],
        'Tác giả': [book.authors],
        'Nhà xuất bản': [book.publisher],
        'Năm xuất bản': [book.year],
        'Số ISBN': [book.ISBN],
        'Trạng thái': [book.status]
    }

    new_book_df = pd.DataFrame(new_book_data)
    # Gộp DataFrame mới vào DataFrame hiện tại
    df = pd.concat([df, new_book_df], ignore_index=True)

    # Ghi lại dữ liệu vào file Excel
    df.to_excel('book.xlsx', index=False)
    return
