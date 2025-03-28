# Ngô Thu Thảo 20216960
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget

from add_book import AddBookWidget
from find_book import FindBookWidget
from delete_book import DeleteBookWidget
from list_book import ListBookWidget
from update_book import UpdateBookWidget


class Menu(QWidget):
    """
    Menu cho chương trình Quản lý thư viện
    """
    def __init__(self):
        super().__init__()
        self.content_widget = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setWindowTitle("QUẢN LÝ THƯ VIỆN")
        self.content_widget = QWidget()

        # Tạo nút hiển thị sách
        button_list_book = QPushButton("THÔNG TIN SÁCH TRONG THƯ VIỆN")
        button_list_book.clicked.connect(self.show_list_book_widget)

        button_find_book = QPushButton("TÌM KIẾM SÁCH")
        button_find_book.clicked.connect(self.show_find_book_widget)

        # Tạo nút "Thêm sách"
        button_add_book = QPushButton("THÊM SÁCH MỚI")
        button_add_book.clicked.connect(self.show_add_book_widget)

        # Tạo nút "Cập nhật sách"
        button_update_book = QPushButton("CẬP NHẬT THÔNG TIN SÁCH")
        button_update_book.clicked.connect(self.show_update_book_widget)

        # Tạo nút "Xóa sách"
        button_delete_book = QPushButton("XÓA THÔNG TIN SÁCH")
        button_delete_book.clicked.connect(self.show_delete_book_widget)

        layout.addWidget(button_list_book)
        layout.addWidget(button_find_book)
        layout.addWidget(button_add_book)
        layout.addWidget(button_update_book)
        layout.addWidget(button_delete_book)
        layout.addWidget(self.content_widget)

        self.setLayout(layout)
        self.show()

    def show_list_book_widget(self):
        self.content_widget = ListBookWidget()
        self.content_widget.show()

    def show_find_book_widget(self):
        self.content_widget = FindBookWidget()
        self.content_widget.show()

    def show_add_book_widget(self):
        self.content_widget = AddBookWidget()
        self.content_widget.show()

    def show_update_book_widget(self):
        self.content_widget = UpdateBookWidget()
        self.content_widget.show()

    def show_delete_book_widget(self):
        self.content_widget = DeleteBookWidget()
        self.content_widget.show()
