# Ngô Thu Thảo 20216960
import pandas as pd
import logging
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from util import find_book


class FindBookWidget(QWidget):
    """
    Giao diện tìm kiếm sách
    """
    def __init__(self):
        super().__init__()
        self.find_button = None
        self.result_label = None
        self.keyword_edit = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.setWindowTitle("TÌM KIẾM THÔNG TIN SÁCH")
        self.result_label = QLabel("Kết quả tìm kiếm:")

        self.keyword_edit = QLineEdit()
        self.keyword_edit.setPlaceholderText("Nhập mã sách, tên sách hoặc số ISBN")
        # Tạo nút
        self.find_button = QPushButton("Tìm sách")
        self.find_button.clicked.connect(self.result)

        layout.addWidget(self.result_label)
        layout.addWidget(self.keyword_edit)
        layout.addWidget(self.find_button)

        self.setLayout(layout)
        self.show()

    def result(self):
        """
        Thực hiện trả ra kết quả khi tìm kiếm sách
        :return:
        """
        keyword = self.keyword_edit.text()
        index = find_book(keyword)
        if index != -1:
            logging.info("Đã tìm thấy sách.")
            book_info = self.get_book_info(index)
            self.result_label.setText(book_info)
        else:
            logging.warning("Không tìm thấy sách")
            self.result_label.setText("Không tìm thấy sách.")

    @staticmethod
    def get_book_info(index):
        """
        Lấy thông tin của sách có index theo file dữ liệu
        :param index: index của sách trong file dữ liệu
        :return:
        """
        try:
            df = pd.read_excel("book.xlsx")
            row = df.iloc[index]
            book_info = f"Mã sách: {row['Mã sách']}\n" \
                        f"Tên sách: {row['Tên sách']}\n" \
                        f"Tác giả: {row['Tác giả']}\n" \
                        f"Nhà xuất bản: {row['Nhà xuất bản']}\n" \
                        f"Năm xuất bản: {row['Năm xuất bản']}\n" \
                        f"Số ISBN: {row['Số ISBN']}\n" \
                        f"Trạng thái: {row['Trạng thái']}"
            return book_info
        except Exception as e:
            logging.warning(f"Lỗi khi lấy thông tin sách: {e}")
            return "Lỗi khi lấy thông tin sách."
