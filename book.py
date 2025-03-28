# Ngô Thu Thảo 20216960
class Book:
    """
    Class Book đại diện cho một cuốn sách với các thuộc tính chính như mã sách, tên sách,
    tác giả, nhà xuất bản, năm xuất bản, số ISBN và trạng thái.
    """
    def __init__(self, bookID, title, authors, publisher, year, ISBN, status):
        self.bookID = bookID  # mã sách
        self.title = title  # tên sách
        self.authors = authors  # tác giả
        self.publisher = publisher  # nhà xuất bản
        self.year = year  # năm xuất bản
        self.ISBN = ISBN  # số ISBN
        self.status = status  # trạng thái

    def display_info(self):
        print("Thông tin sách:")
        print("Mã sách:", self.bookID)
        print("Tên sách:", self.title)
        print("Tác giả:", self.authors)
        print("Nhà xuất bản:", self.publisher)
        print("Năm xuất bản:", self.year)
        print("Số ISBN:", self.ISBN)
        print("Trạng thái:", self.status)
