# Ngô Thu Thảo 20216960
import logging
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

from book import Book
from util import find_book, is_book_id_exists, dataframe


class UpdateBookWidget(QWidget):
    """
    Giao diện cập nhật thông tin sách trong thư viện
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
        self.setWindowTitle("CẬP NHẬT SÁCH")
        layout.addWidget(QLabel("===== CẬP NHẬT THÔNG TIN SÁCH ====="))

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

        layout.addWidget(QLabel("ISBN"))
        self.isbn_edit = QLineEdit()
        layout.addWidget(self.isbn_edit)

        layout.addWidget(QLabel("Trạng thái"))
        self.status_edit = QLineEdit()
        layout.addWidget(self.status_edit)

        # Tạo nút "Xác nhận" để thêm sách mới
        button_confirm = QPushButton("Xác nhận")
        button_confirm.clicked.connect(self.update_book_w)
        layout.addWidget(button_confirm)

        self.setLayout(layout)
        self.show()

    def update_book_w(self):
        # Lấy thông tin sách từ các QLineEdit
        book_id = self.book_id_edit.text()
        title = self.title_edit.text()
        authors = self.authors_edit.text()
        publisher = self.publisher_edit.text()
        year = self.year_edit.text()
        isbn = self.isbn_edit.text()
        status = self.status_edit.text()

        if book_id == '' or title == '' or authors == '':
            # kiểm tra xem mã sách, tên sách hoặc tên giác có để trống
            logging.warning("Mã sách, Tên sách, và Tác giả không được để trống.")
            QMessageBox.warning(self, "Cảnh báo", "Mã sách, Tên sách, và Tác giả không được để trống.")
            return

        if not is_book_id_exists(book_id):
            logging.warning("Mã sách không tồn tại. Không cập nhật thông tin mới.")
            QMessageBox.warning(self, "Cảnh báo", "Mã sách không tồn tại. Không cập nhật thông tin mới.")
            self.ready()
            return

        updated_book = Book(book_id, title, authors, publisher, year, isbn, status)
        update_book(updated_book, book_id)
        logging.info(f"Đã cập nhật thông tin thành công cho sách có mã {book_id}")
        QMessageBox.information(self, "Thông báo", "Đã cập nhật thông tin thành công.")
        self.ready()

    def ready(self):
        """
        Đặt lại các phần để tiếp tục cập nhật cho sách khác
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


def update_book(updatedBook, bookID: str):
    """
    Cập nhật thông tin cho sách có trong thư viện
    :param updatedBook: thông tin cập nhật
    :param bookID: mã sách cần cập nhật
    :return:
    """
    df = dataframe()

    # Cập nhật thông tin sách trong DataFrame
    index = find_book(bookID)
    df.loc[index, 'Tên sách'] = updatedBook.title
    df.loc[index, 'Tác giả'] = updatedBook.authors
    df.loc[index, 'Nhà xuất bản'] = updatedBook.publisher
    df.loc[index, 'Năm xuất bản'] = updatedBook.year
    df.loc[index, 'Số ISBN'] = updatedBook.ISBN
    df.loc[index, 'Trạng thái'] = updatedBook.status

    # Ghi lại dữ liệu vào file Excel
    df.to_excel('book.xlsx', index=False)
