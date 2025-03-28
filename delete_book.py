# Ngô Thu Thảo 20216960
import logging
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox

from util import find_book, is_book_id_exists, dataframe


class DeleteBookWidget(QWidget):
    """
    Giao diện xóa sách có trong thư viện
    """
    def __init__(self):
        super().__init__()
        self.book_id_edit = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("===== XÓA THÔNG TIN SÁCH ====="))

        layout.addWidget(QLabel("Nhập mã sách cần xóa"))
        self.book_id_edit = QLineEdit()
        layout.addWidget(self.book_id_edit)

        # Tạo nút "Xác nhận" để thêm sách mới
        button_confirm = QPushButton("Xác nhận")
        button_confirm.clicked.connect(self.delete_book_w)
        layout.addWidget(button_confirm)

        self.setLayout(layout)
        self.show()

    def delete_book_w(self):
        # Lấy mã sách từ các QLineEdit
        book_id = self.book_id_edit.text()

        if book_id == '':
            # kiểm tra mã sách có để trống không
            logging.warning("Mã sách cần xóa không được để trống.")
            QMessageBox.warning(self, "Cảnh báo", "Mã sách cần xóa không được để trống!")
            return

        if not is_book_id_exists(book_id):
            logging.warning("Mã sách không tồn tại.")
            QMessageBox.warning(self, "Cảnh báo", "Mã sách không tồn tại!")
            self.ready()
            return

        delete_book(book_id)
        logging.info(f"Đã xóa thành công sách có mã {book_id}")
        QMessageBox.information(self, "Thông báo", "Đã xóa sách thành công.")
        self.ready()

    def ready(self):
        """
        Đặt lại để xóa sách khác
        :return:
        """
        self.book_id_edit.clear()
        # Trở về lại focus vào ô nhập mã sách
        self.book_id_edit.setFocus()


def delete_book(bookID: str):
    """
    Xóa sách theo mã sách
    :param bookID: mã sách cần xóa
    :return:
    """
    df = dataframe()

    # Tìm vị trí của sách cần xóa trong DataFrame
    index = find_book(bookID)
    if index != -1:
        # Xóa sách khỏi DataFrame
        df.drop(index, inplace=True)

        # Reset lại chỉ số index trong DataFrame
        df.reset_index(drop=True, inplace=True)

        # Ghi lại dữ liệu vào file Excel
        df.to_excel('book.xlsx', index=False)

    return
