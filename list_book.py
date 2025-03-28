# Ngô Thu Thảo 20216960
import logging
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QHeaderView, QPushButton, QTableWidgetItem

from util import dataframe


class ListBookWidget(QWidget):
    """
    Giao diện hiển thị danh sách các sách đang có trong thư viện
    """

    def __init__(self):
        super().__init__()
        self.table_widget = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setWindowTitle("DANH SÁCH THÔNG TIN SÁCH CỦA THƯ VIỆN")

        # Tạo một QTableWidget để hiển thị danh sách các sách
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(7)
        self.table_widget.setHorizontalHeaderLabels(
            ["Mã sách", "Tên sách", "Tác giả", "Nhà xuất bản", "Năm xuất bản", "Số ISBN", "Trạng thái"]
        )
        self.load_data()
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setAlternatingRowColors(True)

        layout.addWidget(self.table_widget)

        # Thêm nút sắp xếp theo Mã sách
        button_sort_by_book_id = QPushButton("Sắp xếp theo Mã sách")
        button_sort_by_book_id.clicked.connect(self.sort_by_registration)
        layout.addWidget(button_sort_by_book_id)

        # Thêm nút sắp xếp theo Nhà xuất bản
        button_sort_by_publisher = QPushButton("Sắp xếp theo Nhà xuất bản")
        button_sort_by_publisher.clicked.connect(self.sort_by_publisher)
        layout.addWidget(button_sort_by_publisher)

        self.setLayout(layout)
        self.show()

    def load_data(self):
        df = dataframe()
        data = df.values.tolist()

        self.table_widget.setRowCount(len(data))

        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_index, col_index, item)

        # Tùy chỉnh màu sắc cho bảng sách
        for row_index in range(self.table_widget.rowCount()):
            if row_index % 2 == 0:
                for col_index in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row_index, col_index)
                    item.setBackground(QColor("#f2f2f2"))
            else:
                for col_index in range(self.table_widget.columnCount()):
                    item = self.table_widget.item(row_index, col_index)
                    item.setBackground(QColor("#ffffff"))

    def sort_by_registration(self):
        sort_books_by_registration()
        self.load_data()

    def sort_by_publisher(self):
        sort_books_by_publisher()
        self.load_data()


def sort_books_by_registration():
    """
    Sắp xếp sách theo mã sách
    :return:
    """
    df = dataframe()

    # Sắp xếp sách theo Mã sách
    df.sort_values(by='Mã sách', inplace=True)

    # Ghi lại dữ liệu vào file Excel
    df.to_excel('book.xlsx', index=False)
    logging.info("Đã sắp xếp sách theo mã sách.")


def sort_books_by_publisher():
    """
    Sắp xếp sách theo nhà xuất bản
    :return:
    """
    df = dataframe()

    # Sắp xếp sách theo tên nhà xuất bản
    df.sort_values(by='Nhà xuất bản', inplace=True)

    # Ghi lại dữ liệu vào file Excel
    df.to_excel('book.xlsx', index=False)
    logging.info("Đã sắp xếp sách theo tên nhà xuất bản.")
